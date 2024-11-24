
from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# Email Backend Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Replace with your preferred backend

EMAIL_HOST = 'smtp.gmail.com'  # Replace with your email host
EMAIL_PORT = 587  # Replace with your email port
EMAIL_USE_TLS = True  # Set to False if your email server doesn't use TLS
EMAIL_HOST_USER = 'paulnicolas519@gmail.com'  # Replace with your email username
EMAIL_HOST_PASSWORD = 'paul2020'  # Replace with your email password

#classes d’authentification par défaut

AUTH_USER_MODEL = 'accounts.CustomUser'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default='*').split(",")



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    "corsheaders",
    "whitenoise.runserver_nostatic",
    
    # Third party apps
    'rest_framework',
    'rest_framework.authtoken',
     "django_celery_beat",
    
    # Local apps
    'products',
    'accounts',
#    'django_rest_passwordreset', 
    'Commentaires',
    'Hotels',
    'Payements',
    'Reservations',
    'Rooms',
    
    # 'accounts.apps.AccountsConfig',
]



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
 ],

        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 6
    
    # Other settings...
}




#ceci permet de donner le temps vs pouvez modifier le temps en seconde
from datetime import timedelta


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=50),

    }

# Celery Configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Use your preferred message broker here
CELERY_RESULT_BACKEND = 'django-db'  # Use 'redis://' for better performance


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
     "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ALL_ORIGINS = True
