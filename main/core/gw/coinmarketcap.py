
import requests, json, urllib3
from urllib.parse import urlparse, urlencode
from ..utils import is_json

urllib3.disable_warnings()

class CoinMarketCap(object):
	convert_list = ["AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", 
		"HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", 
		"PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"]
	def __init__(self, request, DEBUG=False):
		self.request = request
		self.session = requests.Session()
		self.DEBUG = DEBUG
		self.scheme = "https"
		self.host = "api.coinmarketcap.com"
		self.fixedpath = "v1"
	def ticker(self):
		params = {}
		limit = self.request.POST.get("limit")
		start = self.request.POST.get("start")
		conve = self.request.POST.get("convert", "")
		if limit:
			params["limit"] = limit
		if start:
			params["start"] = start
		if conve and conve in self.convert_list:
			params["convert"] = conve
		return self.__http(resource="ticker/", odt=params,)
	def ticker_id(self, id):
		params = {}
		conve = self.request.POST.get("convert", "")
		if conve and conve in self.convert_list:
			params["convert"] = conve
		return self.__http(resource="ticker/{}/".format(id), odt=params)
	def globale(self):
		params = {}
		conve = self.request.POST.get("convert", "")
		if conve and conve in self.convert_list:
			params["convert"] = conve
		return self.__http(resource="global/", odt=params)
	def __url_encode(self, params, encoding=None):
		return urlencode(params, encoding=encoding)
	def __http(self, resource="", odt="", method="GET", verify=False, res_type="json"):
		self.ispassed, res, url = False, None, "{}://{}/{}/{}".format(self.scheme, self.host, self.fixedpath, resource)
		headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		if method == "HEAD":
			res = self.session.head(url, verify=verify)
		elif method == "GET":
			res = self.session.get(url, params=odt, headers=headers, verify=verify)
		elif method == "POST":
			res = self.session.post(url, data=odt, headers=headers, verify=verify)
		if self.DEBUG:
			print(url)
			print(res.url)
			print(odt)
			print(res.text)
		res_data = ""
		if res_type == "json":
			if res.status_code == requests.codes.ok:
				res_data = res.text
		return res_data

'''
	"id": "bitcoin", 
	"name": "Bitcoin", 
	"symbol": "BTC", 
	"rank": "1", 
	"price_usd": "10990.9", 
	"price_btc": "1.0", 
	"24h_volume_usd": "8105120000.0", 
	"market_cap_usd": "185695377088", 
	"available_supply": "16895375.0", 
	"total_supply": "16895375.0", 
	"max_supply": "21000000.0", 
	"percent_change_1h": "-0.24", 
	"percent_change_24h": "2.1", 
	"percent_change_7d": "7.05", 
	"last_updated": "1519997970"

https://coindelite.com/live-cryptocurrency-price-charts.php

'''