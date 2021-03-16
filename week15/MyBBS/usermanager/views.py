from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from article.models import Article, Comment
from article.serializers import ArticleAPISerializer, CommentAPISerializer
from usermanager.models import UserProfile
from usermanager.serializers import UserProfileRegSerializer, UserProfileSerializer
from utils.permission import IsOwnerOrReadOnly


class UserProfileRegViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    #serializer_class = UserProfileRegSerializer
    authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "create":
            return UserProfileRegSerializer
        return UserProfileSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "create":
            return []
        return [permissions.IsAuthenticated(), IsOwnerOrReadOnly()]

    def create(self, request, *args, **kwargs):
        serializer = UserProfileRegSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['GET'], detail=True, url_path='activities')
    def activities(self, request, *args, **kwargs):
        article = Article.objects.filter(author=request.user.id, alive=True)
        article_serializer = ArticleAPISerializer(article, many=True)

        comment = Comment.objects.filter(author=request.user.id)
        comment_serializer = CommentAPISerializer(comment, many=True)
        result = {
            'article': article_serializer.data if article_serializer else '',
            'comment': comment_serializer.data if comment_serializer else '',
        }

        return Response(result)
