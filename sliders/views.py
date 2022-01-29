from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


from .serializers import SliderSerializer
from .models import Slider


# Create your views here.

class ShowSlider(APIView):
    def get(self,request):
        query=Slider.objects.all()
        #print(query)
        serializers=SliderSerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)


class AddSlider(APIView):
    def post(self,request):
        serializers=SliderSerializer(data=request.data)
        print(request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

