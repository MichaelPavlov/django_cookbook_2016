"""
Django settings for cookbook project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

from utils.misc import get_media_svn_revision
from .conf.dev import *

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x)zqk5i!7l)0u1(y(thg=n&72mcn@equb1*^h-=&59w2ag$_p6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'magazine',
    # 'bulletin_board',
    # 'quotes',
    # 'movies',
    # 'utils',
    # 'cv',
    # 'ideas',
    # 'search',

    # third party apps
    'crispy_forms',
    # 'haystack',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cookbook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'cookbook.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ("en", "English"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("ru", "Русский"),
)
#
# HAYSTACK_CONNECTIONS = {
#     "default": {
#         "ENGINE": "search.multilingual_search_backend.MultilingualWhooshEngine",
#         "PATH": os.path.join(PROJECT_PATH, "cookbook", "tmp", "whoosh_index_ru")
#     },
#     "default_en": {
#         "ENGINE": "search.multilingual_search_backend.MultilingualWhooshEngine",
#         "PATH": os.path.join(PROJECT_PATH, "cookbook", "tmp", "whoosh_index_en")
#     },
#     "default_de": {
#         "ENGINE": "search.multilingual_search_backend.MultilingualWhooshEngine",
#         "PATH": os.path.join(PROJECT_PATH, "cookbook", "tmp", "whoosh_index_de")
#     },
#     "default_fr": {
#         "ENGINE": "search.multilingual_search_backend.MultilingualWhooshEngine",
#         "PATH": os.path.join(PROJECT_PATH, "cookbook", "tmp", "whoosh_index_fr")
#     },
#     "default_ru": {
#         "ENGINE": "search.multilingual_search_backend.MultilingualWhooshEngine",
#         "PATH": os.path.join(PROJECT_PATH, "cookbook", "tmp", "whoosh_index_ru")
#     }
# }

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/%s/' % get_media_svn_revision(BASE_DIR)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/media_root/')

STATIC_ROOT = os.path.join(BASE_DIR, '/static_root/')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'tmp')


# Crispy forms
CRISPY_TEMPLATE_PACK = "bootstrap3"


# Open local settings
try:
    settings_file = os.path.join(os.path.dirname(__file__), "local_settings.py")
    with open(settings_file) as source_file:
        exec(source_file.read())
except IOError:
    pass


