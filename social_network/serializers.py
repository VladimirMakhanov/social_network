from rest_framework.serializers import ModelSerializer
from social_network.models import User, Post


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class  PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'author')
