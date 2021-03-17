from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from usermanager import views

router = routers.DefaultRouter()
router.register('users', views.UserProfileRegViewSet)

urlpatterns = [
    path('', include(router.urls)),
]