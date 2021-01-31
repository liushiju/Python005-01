from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from order import views


router = routers.DefaultRouter()
router.register(r'users', views.UserAPIViewSet)
router.register(r'groups', views.GroupAPIViewSet)
router.register(r'orders', views.OrderAPIViewSet)
router.register(r'shops', views.ShopsAPIViewSet)


urlpatterns = [
    # path(r"login", obtain_jwt_token),
    path("", include(router.urls)),  # 当前路径根目录
    url(r'^api-token-auth/', obtain_jwt_token),
    path(r"api-auth/", include('rest_framework.urls', namespace='rest_framework')),
]
