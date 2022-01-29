from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    class Meta:
        model = Menu
        fields = ('id','name','parent','children')

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'