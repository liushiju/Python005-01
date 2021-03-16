from django_filters.rest_framework import FilterSet

from article.models import Comment


class CommentFilters(FilterSet):
    """自定义过滤类"""

    class Meta:
        model = Comment
        fields = ('aid',)