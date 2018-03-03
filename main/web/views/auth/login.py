# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.shortcuts import HttpResponseRedirect, render, redirect, HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

def login_view(request):
	if request.POST:
		username = request.POST['username'].replace(' ', '').lower()
		password = request.POST['password'].strip()
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			nextto = request.POST.get("next")
			return HttpResponseRedirect(nextto if nextto else reverse("web:home_view"))
		messages.add_message(request, messages.WARNING, _("Username or Password invalid"))
	return render(request, "web/auth/login.html")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("web:login_view"))