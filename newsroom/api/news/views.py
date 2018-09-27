from rest_framework import viewsets
from dry_rest_permissions.generics import DRYObjectPermissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Article
from .serializers import ArticleSeralizer


class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSeralizer
    permission_classes = (DRYObjectPermissions, IsAuthenticatedOrReadOnly)
