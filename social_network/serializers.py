from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.utils.six import text_type
from social_network.models import User, Post, ClearbitInfo, BearerTokens
from social_network.services import verify_email


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, value):

        # raise serializers.ValidationError(value)
        res = verify_email(f'{value}')

        if res['regexp'] is not True:
            raise serializers.ValidationError('Incorrect email')

        if res['smtp_check'] is not True:
            raise serializers.ValidationError('Seems that server doesnt exist')

        if res['disposable'] is True:
            raise serializers.ValidationError('Please don`t use disposable email')

        if res['gibberish'] is True:
            raise serializers.ValidationError('U R okay? Please, input correct email')

        return value


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ClearbitInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClearbitInfo
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        cb = ClearbitInfo(**validated_data)
        cb.save()
        return cb


class BearerTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = BearerTokens
        fields = '__all__'


class BearerTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(self, user):

        token = super(BearerTokenObtainPairSerializer, self).get_token(user)

        token['name'] = user.username

        bt_data = {
            'user': user.pk,
            'refresh_token': text_type(token),
            'lifetime_refresh_token': settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            'access_token': text_type(token.access_token),
            'lifetime_access_token': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],

        }
        return token

    def validate(self, attrs):
        data = super(BearerTokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token)

        return data
