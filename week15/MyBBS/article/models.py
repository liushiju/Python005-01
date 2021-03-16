from django.db import models

from usermanager.models import UserProfile


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="名称")

    class Meta:
        verbose_name = verbose_name_plural = '标签'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    author = models.ForeignKey(UserProfile, related_name='article', blank=True, on_delete=models.DO_NOTHING, verbose_name='作者')
    content = models.TextField('正文')
    alive = models.BooleanField('是否正常', default=True)
    pv = models.PositiveIntegerField(default=1)
    tag = models.ManyToManyField(Tag, null=True,blank=True, verbose_name="标签")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'

    def __str__(self):
        return self.title


class Comment(models.Model):
    aid = models.ForeignKey(Article, related_name='aid', on_delete=models.CASCADE, verbose_name='评论的文章')
    author = models.ForeignKey(UserProfile, related_name='comment', on_delete=models.CASCADE, verbose_name='评论者')
    uid = models.IntegerField(default=0, verbose_name='被回复用户')
    root = models.IntegerField(default=0, verbose_name='根评论')
    parent = models.IntegerField(default=0, verbose_name='父评论')
    content = models.TextField(blank=False, verbose_name='评论内容')
    like = models.IntegerField(default=0, verbose_name='点赞数')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'
