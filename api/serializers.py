from rest_framework import serializers
from .models import Post, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class LikeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user",)


class PostListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(read_only=True, source="user.username")
    likes = LikeShortSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ("id", "user_name", "content", "likes")


class PostDetailSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ("id", "content", "likes")
