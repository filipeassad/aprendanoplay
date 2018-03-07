from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^cadastroaula/', views.cadastroaula),
	url(r'^capivara_adm/', views.capivaraadm),
	url(r'^login/', views.login),
	url(r'^detalhe_curso/', views.detalhe_curso),
	url(r'^lista_cursos/', views.lista_cursos),
	url(r'^area_aluno/', views.area_aluno),
	url(r'^aula_rep/', views.aula_rep),
]