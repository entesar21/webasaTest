from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


from .serializers import ArticleSerializer
from .models import Article




class ShowArticle(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self,request):
        query=Article.objects.all().order_by('created')
        #print(query)
        serializers=ArticleSerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)


class AddArticle(APIView):
    permission_classes = [permissions.IsAdminUser]
    def post(self,request):
        serializers=ArticleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)



