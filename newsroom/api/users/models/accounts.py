import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __repr__(self):
        return f'{self.username}'

    def has_object_update_permission(self, request):
        return request.user.id == self.id

    @staticmethod
    def has_object_read_permission(request):
        return True

    @staticmethod
    def has_object_retrieve_permission(request):
        return True

    @staticmethod
    def has_object_destroy_permission(request):
        return False

    @staticmethod
    def has_object_create_permission(request):
        return True
