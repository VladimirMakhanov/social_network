from django.contrib.auth.models import AbstractUser
from rest_framework.serializers import ModelSerializer
from social_network.models import User, Post


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author')
