# -*- coding: utf-8 -*-
"""
Django 1.11
"""
from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext_lazy as _
import os, environ 

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path('main')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env('.env')

SECRET_KEY = 'zu=)u3q#_kgy9hx=4&gf(@copjc=*cu7p!#c#c#9k=3%m#qnqh'
DEBUG = env.bool("DEBUG", False)

SITE_ID = int(env('SITE_ID', default="1"))

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'django.contrib.admin',
]

LOCAL_APPS = [
    'main.web',
    'main.core',
]

THIRD_PARTY_APPS = [
    'requests',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(APPS_DIR.path('templates')),
        ],
        'APP_DIRS': DEBUG,
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

LANGUAGE_CODE = env('LANGUAGE_CODE', default="en")
TIME_ZONE = env('TIME_ZONE', default="UTC")
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = str(ROOT_DIR('public/static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (str(APPS_DIR.path('static', )),)

MEDIA_ROOT = str(ROOT_DIR('public/media'))
MEDIA_URL = '/media/'

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

DEFAULT_USER_AVATAR = STATIC_URL + "assets/img/user.png"
DEFAULT_USER_FOLDER = "users/"

LOGIN_URL = '/account/login/'
ADMIN_URL = env('ADMIN_URL', default="admin/")

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {
    message_constants.DEBUG: 'info',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}