from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework import status
from social_network.models import User, Post
from social_network.serializers import UserSerializer, PostSerializer


class UserView(ViewSetMixin, ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class PostView(ViewSetMixin, ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

