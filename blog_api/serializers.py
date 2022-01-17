from rest_framework import serializers
from blog_api.models import Category, Post
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



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


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],            
        )
        user.set_password(validated_data["password"])
        user.save()
        return user



# JWT simple token serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token["email"] = user.email
        token["message"] = "Welcome to ShopNext"

        return token

