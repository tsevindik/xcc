from django.conf.urls import url
from .views import *


urlpatterns = [
	url(r'^account/logout/$', logout_view, name="logout_view"),
	url(r'^account/login/$', login_view, name="login_view"),
	url(r'^trade_prices_check/$', trade_prices_check, name="trade_prices_check"),
	url(r"^$", view=home_view, name='home_view'),

]