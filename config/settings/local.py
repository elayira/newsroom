from .common import Common
from .common import env  # , BASE_DIR


class Local(Common):
    DEBUG = True
    SECRET_KEY = env(
        'DJANGO_SECRET_KEY',
        default='UtdFsXdsZpG2j66oM0d30zSJpaMfUDqFrwXD6bH6vMBMfLDjmYaFZDriU3NThc1s'
    )
    ALLOWED_HOSTS = [
        "localhost",
        ".localtest.me",
        ".localtunnel.me",
        "0.0.0.0",
        "127.0.0.1",
    ]

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        # BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=newsroom/api',
    ]

    # CACHES
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#caches
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': ''
        }
    }

    # TEMPLATES
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#templates
    TEMPLATES = Common.TEMPLATES
    TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
    # EMAIL
    # ------------------------------------------------------------------------------
    # https://docs.djangoproject.com/en/dev/ref/settings/#email-host
    EMAIL_HOST = env('EMAIL_HOST', default='mailhog')
    # https://docs.djangoproject.com/en/dev/ref/settings/#email-port
    EMAIL_PORT = 1025

    # django-debug-toolbar
    # ------------------------------------------------------------------------------
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
    INSTALLED_APPS += ['debug_toolbar']  # noqa F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
    MIDDLEWARE = Common.MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']  # noqa F405
    # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
    INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']
    if env('USE_DOCKER') == 'yes':
        import socket
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        INTERNAL_IPS += [ip[:-1] + '1' for ip in ips]
