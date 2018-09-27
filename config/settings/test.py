from .common import Common, env, BASE_DIR


class Test(Common):
    DEBUG = False
    SECRET_KEY = env(
        'DJANGO_SECRET_KEY',
        default='UtdFsXdsZpG2j66oM0d30zSJpaMfUDqFrwXD6bH6vMBMfLDjmYaFZDriU3NThc1s'
    )
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ['django_nose']
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=newsroom/api',
    ]
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': ''
        }
    }
