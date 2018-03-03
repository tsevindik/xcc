# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class WebConfig(AppConfig):
	name = "main.web"
	verbose_name = _("Home")
	verbose_name_plural = _("Home")