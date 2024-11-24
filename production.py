from settings import *
from decouple import config











DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'restapitest',
        'USER': 'postgres',
        'PASSWORD': 'Davide2020@@',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


CELERY_BROKER_URL = config('REDIS_URL', "redis://redis")

CELERY_RESULT_BACKEND = CELERY_BROKER_URL

CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config("REDIS_URL", "redis://redis"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        },
    },
}



DEBUG = False


CSRF_TRUSTED_ORIGINS = [
    "https://sendmoney.com",
    "http://sendmoney.com",
    "http://127.0.0.1",
    "http://localhost",
]

CSRF_COOKIE_DOMAIN = '.sendmoney.com'

