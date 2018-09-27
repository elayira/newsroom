import logging

from .common import Common
from .common import env


class Production(Common):
    # SECURITY
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-ssl-redirect
    SECURE_SSL_REDIRECT = env.bool('DJANGO_SECURE_SSL_REDIRECT', default=True)
    # https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
    SESSION_COOKIE_SECURE = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
    SESSION_COOKIE_HTTPONLY = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
    CSRF_COOKIE_SECURE = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
    CSRF_COOKIE_HTTPONLY = True
    # https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
    # TODO: set this to 60 seconds first and then to 518400 once you prove the former works
    SECURE_HSTS_SECONDS = 60
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool('DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True)
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
    SECURE_HSTS_PRELOAD = env.bool('DJANGO_SECURE_HSTS_PRELOAD', default=True)
    # https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
    SECURE_CONTENT_TYPE_NOSNIFF = env.bool('DJANGO_SECURE_CONTENT_TYPE_NOSNIFF', default=True)
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
    SECURE_BROWSER_XSS_FILTER = True
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = env('DJANGO_SECRET_KEY')
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')
    INSTALLED_APPS += ("gunicorn", )

    # Anymail (Mailgun)
    # ------------------------------------------------------------------------------
    # https://anymail.readthedocs.io/en/stable/installation/#installing-anymail
    INSTALLED_APPS += ['anymail']  # noqa F405
    EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
    # https://anymail.readthedocs.io/en/stable/installation/#anymail-settings-reference
    ANYMAIL = {
        'MAILGUN_API_KEY': env('MAILGUN_API_KEY'),
        'MAILGUN_SENDER_DOMAIN': env('MAILGUN_DOMAIN')
    }

    # EMAIL
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
    DEFAULT_FROM_EMAIL = env(
        'DJANGO_DEFAULT_FROM_EMAIL',
        default='newsroom <noreply@ayira.net>'
    )
    # https://docs.djangoproject.com/en/dev/ref/settings/#server-email
    SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)
    # https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
    EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[newsroom]')

    # ADMIN
    # ------------------------------------------------------------------------------
    # Django Admin URL regex.
    ADMIN_URL = env('DJANGO_ADMIN_URL')

    # DATABASES
    # ------------------------------------------------------------------------------
    DATABASES = Common.DATABASES
    DATABASES['default'] = env.db('DATABASE_URL')  # noqa F405
    DATABASES['default']['ATOMIC_REQUESTS'] = True  # noqa F405
    DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)  # noqa F405

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # http://django-storages.readthedocs.org/en/latest/index.html
    INSTALLED_APPS += ('storages',)
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_AUTO_CREATE_BUCKET = True
    AWS_QUERYSTRING_AUTH = False
    MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'

    # https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#cache-control
    # Response can be cached by browser and any intermediary caches (i.e. it is "public") for up to 1 day
    # 86400 = (60 seconds x 60 minutes x 24 hours)
    AWS_HEADERS = {
        'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
    }
    # CACHES
    # ------------------------------------------------------------------------------
    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': env('REDIS_URL'),
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                # Mimicing memcache behavior.
                # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
                'IGNORE_EXCEPTIONS': True,
            }
        }
    }
    # raven
    # ------------------------------------------------------------------------------
    # https://docs.sentry.io/clients/python/integrations/django/
    INSTALLED_APPS += ['raven.contrib.django.raven_compat']  # noqa F405
    MIDDLEWARE = [
        'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware'
    ] + Common.MIDDLEWARE
    # Sentry
    # ------------------------------------------------------------------------------
    SENTRY_DSN = env('DJANGO_SENTRY_DSN')
    SENTRY_CLIENT = env('DJANGO_SENTRY_CLIENT', default='raven.contrib.django.raven_compat.DjangoClient')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s ' '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.security.DisallowedHost': {
                'level': 'ERROR',
                'handlers': ['console', 'sentry'],
                'propagate': False,
            },
        },
    }
    SENTRY_CELERY_LOGLEVEL = env.int('DJANGO_SENTRY_LOG_LEVEL', logging.INFO)
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN
    }
