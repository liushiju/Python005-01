from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    profile = models.CharField(max_length=200, verbose_name="个人简介")
    points = models.IntegerField(default=0, verbose_name='积分')

    class Meta:
        verbose_name = verbose_name_plural = '用户'

    def __str__(self):
        return self.username