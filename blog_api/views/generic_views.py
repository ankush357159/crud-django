from rest_framework import generics
from blog_api.models import Category, Post
from blog_api.serializers import CategorySerializer, MyTokenObtainPairSerializer, PostSerializer, RegisterUserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


# JWT simple token view
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny,]
    serializer_class = MyTokenObtainPairSerializer   

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [IsAuthenticated,]