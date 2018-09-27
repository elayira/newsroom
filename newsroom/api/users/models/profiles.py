import uuid

from django.db import models
from django.conf import settings


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(max_length=550, blank=True, null=True, default='')

    def has_object_update_permission(self, request):
        return request.user == self.user

    @staticmethod
    def has_object_read_permission(request):
        return True

    @staticmethod
    def has_object_retrieve_permission(request):
        return True

    def __repr__(self):
        return f'{self.user}'
