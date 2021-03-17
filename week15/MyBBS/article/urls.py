from django.urls import path, include
from rest_framework import routers

from article import views

router = routers.DefaultRouter()
router.register('articles', views.ArticleAPIViewSet)
router.register('comments', views.CommentAPIViewSet)
router.register('tags', views.TagAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]