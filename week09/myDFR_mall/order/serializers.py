from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User, Group
from rest_framework import serializers

from order.models import Order, Shops


class ShopsAPISerializer(serializers.HyperlinkedModelSerializer):
    """商品序列"""

    class Meta:
        model = Shops
        # fields = ('url', 'name', 'price')
        fields = '__all__'


class OrderAPISerializer(serializers.HyperlinkedModelSerializer):
    """订单序列"""

    class Meta:
        model = Order
        fields = '__all__'
        # exclude = ('create_time','alive')


class UserAPISerializer(serializers.HyperlinkedModelSerializer):
    """用户序列"""

    order = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'order', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        """对密码进行加密"""
        attrs['password'] = make_password(attrs['password'])
        return attrs


class GroupAPISerializer(serializers.HyperlinkedModelSerializer):
    """组序列"""

    class Meta:
        model = Group
        fields = ('url', 'name')
