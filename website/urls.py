from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .import views


urlpatterns = [
	url(r'^cadastroaula', views.cadastroaula),
	url(r'^capivara_adm', views.capivaraadm),
	url(r'', views.index),
]