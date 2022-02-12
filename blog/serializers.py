from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
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