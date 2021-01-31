from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Shops(models.Model):

    __tablename__ = 'goods'
    name = models.CharField(max_length=30, verbose_name="名称")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="价格")
    alive = models.BooleanField(default=True, verbose_name="在售")
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['create_time']

    def __str__(self):
        return self.name


class Order(models.Model):

    __tablename__ = 'order'
    user = models.ForeignKey('auth.User', verbose_name='用户id', related_name='order', on_delete=models.CASCADE)
    shops = models.ForeignKey('Shops', verbose_name='商品', related_name='order', on_delete=models.CASCADE)
    count = models.IntegerField(blank=True, null=True, verbose_name="数量")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="金额")
    alive = models.BooleanField(default=True, verbose_name="有效")
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shops.name

    class Meta:
        ordering = ['create_time']