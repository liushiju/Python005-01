from django.shortcuts import render
from django_redis import get_redis_connection
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from article.filter import CommentFilters
from article.models import Article, Comment, Tag
from article.serializers import ArticleAPISerializer, CommentAPISerializer, TagAPISerializer
from usermanager.models import UserProfile
from permissions import IsOwnerOrReadOnly


class ArticleAPIViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-created_time')
    serializer_class = ArticleAPISerializer
    pagination_class = PageNumberPagination
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    search_fields = ['title', 'content']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = request.user
        author.points += 1
        serializer.save()
        author.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.alive:
            return Response(status=status.HTTP_404_NOT_FOUND)
        num = get_cache_counter(kwargs['pk'])
        instance.pv = num
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        try:
            article = self.get_object()
            article.alive = False
            article.save()
            return Response(status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CommentAPIViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentAPISerializer
    pagination_class = PageNumberPagination
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filter_class = CommentFilters

    def create(self, request, *args, **kwargs):
        user = request.user
        user.points += 1

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user.save()

        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        if request.query_params.get('aid') is None:
            return Response(status=status.HTTP_403_FORBIDDEN)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TagAPIViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagAPISerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated]


def get_cache_counter(aid):
    cache = get_redis_connection()
    return cache.incr(aid)