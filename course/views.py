from .serializers import *
from .models import *

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions, mixins
from rest_framework.exceptions import ValidationError

from django.db.models import Sum


class ShowCourse(APIView):
    def get(self,request):
        query=Course.objects.all()
        serializers=CourseSerializer(query,many=True,context={ 'request' : request})
        return Response(serializers.data,status=status.HTTP_200_OK)


class AddCourse(APIView):
    def post(self,request):
        serializers=CourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class NumberOfCourses(APIView):
    def get(self, request):
        query = Course.objects.count()
        serializers = CourseSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)


class SumCourseDuration(APIView):
    def get(self, request):
        query = Course.objects.aggregate(Sum('course_duration'))
        serializers = CourseSerializer(query)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ShowCourseCategory(APIView):
    def get(self,request):
        query=CourseCategory.objects.all()
        serializers=CourseCategorySerializer(query,many=True,context={ 'request' : request})
        return Response(serializers.data,status=status.HTTP_200_OK)


class CommentRelatedToCourse(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, pk):
        query = Comment.objects.filter(course=pk , active=True)
        serializer = CommentSerializer(query, many=True, context={'request' : request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        comment = Comment.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, comment=comment)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError ('you have already voted for this post :)')
        serializer.save(voter=self.request.user, comment=Comment.objects.get(pk=self.kwargs['pk']))

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('you never voted for this post...silly!')






