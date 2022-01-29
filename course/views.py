from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


from .serializers import CourseSerializer
from .models import Course


# Create your views here.

class ShowCourse(APIView):
    def get(self,request):
        query=Course.objects.all()
        #print(query)
        serializers=CourseSerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)


class AddCourse(APIView):
    def post(self,request):
        serializers=CourseSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

