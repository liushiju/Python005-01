from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from article.serializers import ArticleAPISerializer
from usermanager.models import UserProfile


class UserProfileRegSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        help_text="密码", label="密码", write_only=True,
    )

    class Meta:
        model = UserProfile
        fields = ('username', 'password')

    def validate(self, attrs):
        attrs['password'] = make_password(attrs['password'])
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    article = ArticleAPISerializer(read_only=True, many=True)

    class Meta:
        model = UserProfile
        fields = ('url', 'id', 'username', 'password', 'email', 'profile', 'points', 'article')
        extra_kwargs = {
            'password': {'write_only': True},
            'points': {'read_only': True},
        }

    def validate(self, attrs):
        """对密码进行加密"""
        attrs['password'] = make_password(attrs['password'])
        return attrs