from rest_framework import permissions as rest_permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from social_network import permissions as social_permissions
from social_network.models import User, Post
from social_network.serializers import UserSerializer, PostSerializer, BearerTokenObtainPairSerializer


class UserView(ViewSetMixin, ListAPIView, CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (social_permissions.CreateUserPermission,)


class PostView(ViewSetMixin, ListAPIView, CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (rest_permissions.IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        post_data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'author': request.user.pk,
        }
        post = PostSerializer(data=post_data)

        if post.is_valid(raise_exception=True):
            post.create(post.validated_data)
            return Response(status=status.HTTP_200_OK)

        else:
            return Response(data=post.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], url_path='like', detail=True)
    def like(self, request, *args, **kwargs):
        # return Response(kwargs)
        post = Post.objects.get(pk=kwargs.get('pk'))
        user = request.user
        likes = user.likes.filter(id=post.pk)

        if likes.count():
            User.likes.through.objects.get(user__id=user.pk, post__id=post.pk).delete()

        else:
            user.likes.add(post)

        return Response(likes.count())


class BearerTokenObtainPairView(TokenObtainPairView):
    serializer_class = BearerTokenObtainPairSerializer


class BearerTokenRefreshView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer
