from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    vote = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1
    def get_vote(self, comment):
        return Vote.objects.filter(comment=comment).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']

