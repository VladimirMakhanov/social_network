from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from social_network.models import User, Post, ClearbitInfo
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
        fields = ('title', 'content', 'author')


class ClearbitInfoSerializer(serializers.ModelSerializer):

    # user = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # user = UserSerializer()

    class Meta:
        model = ClearbitInfo
        fields = '__all__'

    def validate(self, attrs):
        # raise serializers.ValidationError(attrs['user'].pk)
        return attrs

    def create(self, validated_data):
        # print('=============')
        # print(self.data['user'])
        # print(validated_data['user'])
        # user = validated_data.pop('user')
        cb = ClearbitInfo(**validated_data)
        cb.save()
        return cb

    # def validate_user(self, value):
    #     raise serializers.ValidationError(f"value = {value}")


    # def validate_utcOffset(self, value):
    #     print(value)
    #     if value == '':
    #         return None
    #     elif isinstance(value, int):
    #         return value
    #     else:
    #         raise ValidationError('"A valid integer is required.')
