from rest_framework.routers import DefaultRouter

from .views import ArticleViewset

app_name = 'news'

urlpatterns = DefaultRouter()
urlpatterns.register('news', ArticleViewset, base_name='article')
