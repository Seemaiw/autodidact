from django.shortcuts import render
from rest_framework import viewsets, generics

# Create your views here.
from post.models import Post, Category
from post.serializers import PostReadSerializer, CategorySerializer


class  PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostReadSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer