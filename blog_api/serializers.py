from rest_framework import serializers
from blog_api.models import Category, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'body', 'created', 'status','slug','category',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']



