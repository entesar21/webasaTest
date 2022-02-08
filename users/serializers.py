from rest_framework import serializers
from .models import *


#get channel(Phone or Email) and receiver(the phone number or the email address) from user
class RequestOTPSerializer(serializers.Serializer):
    receiver=serializers.CharField(max_length=50,allow_null=False)
    channel=serializers.ChoiceField(allow_null=False,choices=OTPRequest.OtpChannel.choices)

#sending request_id to user and he already has the password sent to his phone
class RequestOTPResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=OTPRequest
        fields=['request_id']



#for verifing user should send the request_id and password and receiver
class VerifyOtpRequestSerializer(serializers.Serializer):
    request_id= serializers.UUIDField(allow_null=False)
    password=serializers.CharField(max_length=4,allow_null=False)
    receiver=serializers.CharField(max_length=64,allow_null=False)


#after verifing we send token and refresh token to user created feild is a flag to show its created now or before
class ObtainTokenSerializer(serializers.Serializer):
    token=serializers.CharField(max_length=128,allow_null=False)
    refresh=serializers.CharField(max_length=128,allow_null=False)
    created=serializers.BooleanField()

#------------------------------profile serializer---------------------------------#

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= '__all__'




class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id', 'user', 'code_melli' , 'gender' ,'biography' , 'registration_date' ,'profile_image']

        depth = 1


