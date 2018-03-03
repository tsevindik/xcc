# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from main.web import urls as home_urls

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^', include(home_urls, namespace="web", app_name="web")),
]
