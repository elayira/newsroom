
from rest_framework import routers
from .api.news.urls import urlpatterns as news_urls
from .api.users.urls import urlpatterns as user_urls


urlpatterns = routers.DefaultRouter()

urlpatterns.registry.extend(news_urls.registry)
urlpatterns.registry.extend(user_urls.registry)

urlpatterns = urlpatterns.urls
