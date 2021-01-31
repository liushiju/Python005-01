from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from order.serializers import *


class UserAPIViewSet(viewsets.ModelViewSet):
    """
    允许用户查看的或编辑的用户 API 路径.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserAPISerializer

    def create(self, request, *args, **kwargs):
        serializer = UserAPISerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class GroupAPIViewSet(viewsets.ModelViewSet):
    """
    允许用户查看的或编辑的 API 路径.
    """
    queryset = Group.objects.all()
    serializer_class = GroupAPISerializer


class OrderAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """
    允许用户查看的或编辑的订单 API 路径.
    """
    queryset = Order.objects.all()
    serializer_class = OrderAPISerializer
    # 分页功能
    pagination_class = PageNumberPagination  

    @action(methods=["GET"], detail=True)
    def cancel(self, request, *args, **kwargs):
        """
        只接受一个 GET 取消一个订单。
        """
        try:
            order = self.get_object()
            order.alive = False
            order.save()
            return Response(status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=["POST"],
            detail=False,
            url_path='create',
            permission_classes=[IsAuthenticated],   # 用户控制
            authentication_classes=[JSONWebTokenAuthentication])  # JWT 验证
    def create_order(self, request, *args, **kwargs):
        """
        只接受一个 POST 创建一个订单, 该方法仅可 JWT 验证使用
        """
        serizelizer = OrderAPISerializer(data=request.data, context={'request': request})
        serizelizer.is_valid(raise_exception=True)
        serizelizer.save()

        return Response(status.HTTP_201_CREATED)


class ShopsAPIViewSet(viewsets.ModelViewSet):
    """
    允许用户查看的或编辑的商品 API 路径.
    """
    queryset = Shops.objects.all()
    serializer_class = ShopsAPISerializer
