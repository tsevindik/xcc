# -*- coding: utf-8 -*-
from .com import *  # noqa

DATABASES = {
    'default': env.db('SQLITE3_URL', default='sqlite:///db.sqlite3')
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

SECRET_KEY = env("SECRET_KEY", default='6uu&o=8t#rwf@w9!94$a+-m+d5vc6+twkv_+kf&(x798qg_#om')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])