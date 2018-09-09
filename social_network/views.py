from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from social_network.models import User, Post
from social_network.serializers import UserSerializer, PostSerializer
from social_network.permissions import CreatePermission


class UserView(ViewSetMixin, ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (CreatePermission, )


class PostView(ViewSetMixin, ListAPIView, CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (permissions.IsAuthenticated, )

