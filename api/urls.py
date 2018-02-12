from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
	url(r'^perfil', views.ApiPerfil.as_view()),
	url(r'^professores', views.ApiProfessor.as_view()),
	url(r'^endereco', views.ApiEndereco.as_view()),		
	url(r'^curso', views.ApiCurso.as_view()),		
	url(r'^modulo', views.ApiModulo.as_view()),
	url(r'^modulo/(?P<id>\w+)/$', views.ApiModulo.as_view()),
	url(r'^aula', views.ApiAula.as_view()),
	url(r'^documento', views.ApiDocumento.as_view()),
	url(r'^duvida', views.ApiDuvida.as_view()),	
	url(r'^resposta', views.ApiResposta.as_view()),
	url(r'^plano', views.ApiPlano.as_view()),
	url(r'^assinatura', views.ApiAssinatura.as_view()),
	url(r'^situacao', views.ApiSituacao.as_view()),
	url(r'^perfilassinatura', views.ApiPerfilAssinatura.as_view()),
	url(r'^cadastrousuario', views.CadastroUsuario.as_view()),
]