from rest_framework import serializers

from article.models import Article, Tag, Comment


class TagAPISerializer(serializers.ModelSerializer):
    """标签序列"""

    class Meta:
        model = Tag
        fields = "__all__"


class ArticleAPISerializer(serializers.ModelSerializer):
    """文章序列"""
    #tag = TagAPISerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = ('url', 'id', 'title', 'author', 'content', 'tag', 'pv', 'created_time')
        extra_kwargs = {
            'created_time': {'read_only': True},
            'pv': {'read_only': True},
            'author': {'required': False},
            'tag': {'required': False},
        }

    def create(self, validated_data):
        validated_data['author'] = self.context["request"].user
        return super().create(validated_data)


class CommentAPISerializer(serializers.ModelSerializer):
    """评论序列"""

    class Meta:
        model = Comment
        fields = ('url', 'id', 'aid', 'uid', 'root', 'parent', 'author', 'content', 'created_time')
        extra_kwargs = {
            'created_time': {'read_only': True},
            'author': {'required': False},
            'uid': {'required': False},
            'root': {'required': False},
            'parent': {'required': False},
        }