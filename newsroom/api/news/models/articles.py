import uuid
from django.db import models
from django.conf import settings

from django_extensions.db.fields import AutoSlugField
from model_utils.models import StatusModel, TimeStampedModel
from model_utils import Choices
from dry_rest_permissions.generics import authenticated_users


class Article(StatusModel, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=3500)
    STATUS = Choices('draft', 'published')
    slug = AutoSlugField(populate_from=['title'])

    @property
    def author_name(self):
        return self.author.get_full_name()

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_object_read_permission(request):
        return True

    @authenticated_users
    def has_object_write_permission(self, request):
        return self.author == request.user

    @authenticated_users
    def has_write_permission(self, request):
        return self.author == request.user
