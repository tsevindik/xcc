# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.shortcuts import HttpResponseRedirect, render, redirect, HttpResponse
from django.core.urlresolvers import reverse

from main.core.utils import is_json
from main.core.gw import CoinMarketCap
from operator import is_not
from functools import partial
import re, json

def home_view(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect(reverse("web:login_view"))
	return render(request, "web/content/home.html", {})

def trade_prices_check(request):
	args = "{}"
	cmc = CoinMarketCap(request=request, DEBUG=False)
	response = cmc.ticker()
	if is_json(response):
			args = response
			search = request.POST.get("search")
			if search:
				def searchinlist(dt):
					matched = False
					pattern = re.compile(re.escape(search))
					if re.search(pattern, "{}".format(dt.get("name"))) or re.search(pattern, "{}".format(dt.get("id"))):
						matched = True
					return dt if matched else None
				args = json.dumps(list(filter(partial(is_not, None), map(searchinlist, json.loads(args)))))
	return HttpResponse(args, content_type="application/json")

def trade_prices_check_detail(request, cid):
	args = {}
	