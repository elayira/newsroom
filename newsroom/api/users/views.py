from rest_framework import viewsets, generics

from dry_rest_permissions.generics import DRYObjectPermissions

from .serializers import UserSerializer, ProfileSerializer
from .models import User, Profile


class UserViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves user accounts
    """
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (DRYObjectPermissions,)
    http_method_names = [u'get', u'post', u'patch', u'head', u'options', u'trace']


class UserProfileViewSet(generics.RetrieveUpdateAPIView, viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (DRYObjectPermissions, )
