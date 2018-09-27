from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'newsroom.api.users'
    label = 'users'

    def ready(self):
        from . import signals  # noqa
