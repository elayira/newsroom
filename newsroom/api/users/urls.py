from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserProfileViewSet

app_name = 'users'
urlpatterns = DefaultRouter()
urlpatterns.register(r'users', UserViewSet, base_name='user')
urlpatterns.register(r'profile', UserProfileViewSet, base_name='profile')
