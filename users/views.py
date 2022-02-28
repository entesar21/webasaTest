from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import OTPRequest,User,Profile

class OTPView(APIView):
    def get(self, request):
        serializer = RequestOTPSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            otp = OTPRequest.objects.generate(data)
            return Response(data=RequestOTPResponseSerializer(otp).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


    def post(self, request):
        # print(request.data)
        serializer = VerifyOtpRequestSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data['receiver'])
            print(data['request_id'])
            print(data['password'])
            if OTPRequest.objects.is_valid(data['receiver'], data['request_id'], data['password']):
                print('accepted and we are passed')
                return Response(self._handle_login(data))
            else:
                print('401 error')
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            print('400 error')
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def _handle_login(self,otp):
        User=get_user_model()
        query= User.objects.filter(username=otp['receiver'])
        if query.exists():
            created= False
            user= query.first()
        else:
            user= User.objects.create(username=otp['receiver'])
            created= True
        refresh =RefreshToken.for_user(user)

        return ObtainTokenSerializer({
            'refresh': str(refresh),
            'token': str(refresh.access_token),
            'created': created

        }).data


#------------------------profile---------------------#


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        profile = Profile.objects.all()
        return profile

class ProfileApi(APIView):
    def get(self,request,pk):
        query=Profile.objects.get(user_id=pk)
        print(query)
        serializers=ProfileSerializer(query)
        print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)

class ProfileEditApi(APIView):
    def patch(self,request):
        print(Profile.objects.get(user=request.user))
        profile_obj = Profile.objects.get(user=request.user)
        data=request.data

        try:
            user=User.objects.get(id=request.user.id)
            user.first_name = data.get("user.first_name", user.first_name)
            user.last_name = data.get("user.last_name", user.last_name)
            user.email = data.get("user.email", user.email)
            user.save()

        except KeyError:
            pass

        print(data.get("user.first_name"))
        print(user.first_name)
        profile_obj.gender = data.get("gender", profile_obj.gender)
        profile_obj.code_melli = data.get("code_melli", profile_obj.code_melli)
        profile_obj.biography = data.get("biography", profile_obj.biography)


        profile_obj.save()
        serializers = ProfileSerializer(profile_obj)
        return Response(serializers.data,status=status.HTTP_201_CREATED)

    # def put(self,request,pk):
    #     query=Profile.objects.get(pk=pk)
    #     serializers=ProfileSerializer(query, data=request.data)
    #     if serializers.is_valid():
    #         serializers.save()
    #         return Response(serializers.data,status=status.HTTP_201_CREATED)
    #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
