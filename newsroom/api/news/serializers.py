from rest_framework import serializers
from .models import Article


class ArticleSeralizer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='article-detail',
        lookup_field='pk'
    )
    author = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True,
        lookup_field='username'
    )

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            validated_data['author'] = user

        article = Article(**validated_data)
        article.save()
        return article

    class Meta:
        model = Article
        fields = ['title', 'body', 'status', 'author_name', 'created', 'modified', 'author', 'url', 'id']
