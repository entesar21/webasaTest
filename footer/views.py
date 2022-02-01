from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


from .serializers import FooterSerializer
from .models import Footer


# Create your views here.

class ShowFooter(APIView):
    def get(self,request):
        query=Footer.objects.all()
        #print(query)
        serializers=FooterSerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)



class AddFooter(APIView):
    def post(self,request):
        serializers=FooterSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class EditFooter(APIView):

    def patch(self,request):
        footer_obj=Footer.objects.first()
        data=request.data

        footer_obj.footer_about_us = data.get("footer_about_us",footer_obj.footer_about_us)
        footer_obj.footer_telegram = data.get("footer_telegram",footer_obj.footer_telegram)
        footer_obj.footer_insta = data.get("footer_insta",footer_obj.footer_insta)
        footer_obj.footer_whats_app = data.get("footer_whats_app",footer_obj.footer_whats_app)


        footer_obj.footer_aparat = data.get("footer_aparat",footer_obj.footer_aparat)
        footer_obj.footer_youtube = data.get("footer_youtube",footer_obj.footer_youtube)
        footer_obj.footer_twitter = data.get("footer_twitter",footer_obj.footer_twitter)
        footer_obj.footer_linkedin = data.get("footer_linkedin",footer_obj.footer_linkedin)
        footer_obj.footer_address = data.get("footer_address",footer_obj.footer_address)
        footer_obj.footer_phone = data.get("footer_phone", footer_obj.footer_phone)
        footer_obj.footer_facebook = data.get("footer_facebook", footer_obj.footer_facebook)

        footer_obj.save()
        serializers = FooterSerializer(footer_obj)
        return Response(serializers.data,status=status.HTTP_201_CREATED)




from django.shortcuts import render

# Create your views here.
