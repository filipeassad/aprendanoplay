#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponse
from .serializers import *
from rest_framework.response import Response
from website.models import *
import requests
import json
import xml.etree.ElementTree as ET

class ApiPerfil(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		perfil = Perfil(id_endereco=data.get('id_endereco'),
					  nome=data.get('nome'),
					  cpf=data.get('cpf'),
					  email=data.get('email'),
					  data_nasc=data.get('data_nasc'),
					  telefone=data.get('telefone'),
					  tipo_perfil=data.get('tipo_perfil'))

		try:
			perfil.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		perfil = Perfil.objects.all()
		serializer = PerfilSerializer(perfil, many=True)
		return Response(serializer.data)

class ApiProfessor(APIView):
	def get(self, request, *args, **kwargs):
		perfil = Perfil.objects.filter(tipo_perfil="Professor")
		serializer = PerfilSerializer(perfil, many=True)
		return Response(serializer.data)

class ApiEndereco(APIView):
	#authentication_classes = (SessionAuthentication, BasicAuthentication)
	#permission_classes = (IsAuthenticated,)

	def post(self, request, *args, **kwargs):

		data = request.data
		endereco = Endereco(logradouro= data.get('logradouro'),
							numero=data.get('numero'),
							bairro=data.get('bairro'),
							uf=data.get('uf'),
							pais=data.get('pais'),
							cep=data.get('cep'),
							complemento=data.get('complemento'))
		try:
			endereco.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		endereco = Endereco.objects.all()
		serializer = EnderecoSerializer(endereco, many=True)
		return Response(serializer.data)

class ApiCurso(APIView):

	def post(self, request, *args, **kwargs):

		data = request.data
		
		if data.get('tp_req') == "inserir": 

			perfil = Perfil.objects.get(id=data.get('id_perfil'))
			
			curso = Curso(id_perfil=perfil,
						  nome=data.get('nome'),
						  descricao=data.get('descricao'))

			try:
				curso.save()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")

		elif data.get('tp_req') == "editar":

			perfil = Perfil.objects.get(id=data.get('id_perfil'))
			curso = Curso.objects.get(id=data.get('id'))
			curso.id_perfil = perfil
			curso.nome = data.get('nome')
			curso.descricao = data.get('descricao')

			try: 
				curso.save()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")

		elif data.get('tp_req') == "deletar":

			curso = Curso.objects.get(id=data.get('id'))
			try:
				curso.delete()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")
		return HttpResponse("sem sucesso")

	def get(self, request, *args, **kwargs):
		curso = Curso.objects.all()
		serializer = CursoSerializer(curso, many=True)
		return Response(serializer.data)

class ApiModulo(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data

		if data.get('tp_req') == "inserir":

			curso = Curso.objects.get(id=data.get('id_curso'))			
		
			modulo = Modulo(id_curso=curso,
						  nome=data.get('nome'),
						  descricao=data.get('descricao'))

			try:
				modulo.save()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")

		if data.get('tp_req') == "editar":

			curso = Curso.objects.get(id=data.get('id_curso'))
			modulo = Modulo.objects.get(id=data.get('id'))

			modulo.nome = data.get('nome')
			modulo.descricao = data.get('descricao')
			modulo.id_curso = curso

			try:
				modulo.save()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")

		if data.get('tp_req') == "deletar":

			modulo = Modulo.objects.get(id=data.get('id'))
			try:
				modulo.delete()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")						

		return HttpResponse("sem sucesso")

	def get(self, request, *args, **kwargs):
		
		if request.query_params.get('id') is not None: 
			print(request.query_params)
			
			curso = Curso.objects.get(id=request.query_params.get('id'))
			modulo = Modulo.objects.filter(id_curso=curso)
			serializer = ModuloSerializer(modulo, many=True)
			return Response(serializer.data)
		else:
			modulo = Modulo.objects.all()
			serializer = ModuloSerializer(modulo, many=True)
			return Response(serializer.data)

		return HttpResponse(("sem sucesso").encode('utf8'))

class ApiAula(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data

		if data.get('tp_req') == "inserir":

			modulo = Modulo.objects.get(id=data.get('id_modulo'))
			aula = Aula(id_modulo=modulo,
						  nome=data.get('nome'),
						  url_aula=data.get('url_aula'),					  
						  descricao=data.get('descricao'))

			try:
				aula.save()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")

		if data.get('tp_req') == "editar":

			modulo = Modulo.objects.get(id=data.get('id_modulo'))
			aula = Aula.objects.get(id=data.get('id'))

			aula.nome = data.get('nome')
			aula.descricao = data.get('descricao')
			aula.id_modulo = modulo
			aula.url_aula = data.get('url_aula')

			try:
				aula.save()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")

		if data.get('tp_req') == "deletar":
			
			aula = Aula.objects.get(id=data.get('id'))
			
			try:
				aula.delete()
				return HttpResponse("sucesso")
			except:
				pass
			return HttpResponse("sem sucesso")	 

		return HttpResponse("sem sucesso")

	def get(self, request, *args, **kwargs):
		aula = Aula.objects.all()
		serializer = AulaSerializer(aula, many=True)
		return Response(serializer.data)

class ApiDocumento(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		documento = Documento(id_aula=data.get('id_aula'),
					  nome=data.get('nome'),
					  url_arquivo=data.get('url_arquivo'),					  
					  descricao=data.get('descricao'))

		try:
			documento.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		documento = Documento.objects.all()
		serializer = DocumentoSerializer(documento, many=True)
		return Response(serializer.data)

class ApiDuvida(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		duvida = Duvida(id_aula=data.get('id_aula'),
					  titulo=data.get('titulo'),					  					  
					  descricao=data.get('descricao'),
					  data_criacao=datetime.now())

		try:
			duvida.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		duvida = Duvida.objects.all()
		serializer = DuvidaSerializer(duvida, many=True)
		return Response(serializer.data)

class ApiResposta(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		resposta = Resposta(id_duvida=data.get('id_duvida'),					  					  
					  descricao=data.get('descricao'),
					  data_criacao=datetime.now())

		try:
			resposta.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		resposta = Resposta.objects.all()
		serializer = RespostaSerializer(resposta, many=True)
		return Response(serializer.data)

class ApiPlano(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		plano = Plano(id_curso=data.get('id_curso'),					  					  
					  id_pagseguro=data.get('id_pagseguro'),
					  valor=data.get('valor'),
					  periodo=data.get('periodo'))

		try:
			plano.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		plano = Plano.objects.all()
		serializer = PlanoSerializer(plano, many=True)
		return Response(serializer.data)

class ApiAssinatura(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		assinatura = Assinatura(id_plano=data.get('id_plano'),					  					  
					  id_pagseguro=data.get('id_pagseguro'),
					  data_assi=data.get('data_assi'))

		try:
			assinatura.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		assinatura = Assinatura.objects.all()
		serializer = AssinaturaSerializer(assinatura, many=True)
		return Response(serializer.data)

class ApiSituacao(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		situacao = Situacao(id_assinatura=data.get('id_assinatura'),					  					  
					  descricao=data.get('descricao'),
					  data_criacao=data.get('data_criacao'))

		try:
			situacao.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		situacao = Situacao.objects.all()
		serializer = SituacaoSerializer(situacao, many=True)
		return Response(serializer.data)

class ApiPerfilAssinatura(APIView):
	def post(self, request, *args, **kwargs):
		
		data = request.data
		
		perfilassinatura = PerfilAssinatura(id_perfil=data.get('id_perfil'),					  					  
					  id_assinatura=data.get('id_assinatura'))

		try:
			perfilassinatura.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")

	def get(self, request, *args, **kwargs):
		perfilassinatura = PerfilAssinatura.objects.all()
		serializer = PerfilAssinaturaSerializer(perfilassinatura, many=True)
		return Response(serializer.data)

class CadastroUsuario(APIView):
	def post(self, request, *args, **kwargs):
		data = request.data
		usuario = User.objects.create_user(username=data.get('nomeusuario'),
										email=data.get('email'),
										password=data.get('senha'))
		
		perfil = Perfil(id_endereco=data.get('id_endereco'),
					  nome=data.get('nome'),
					  cpf=data.get('cpf'),
					  email=data.get('email'),
					  data_nasc=data.get('data_nasc'),
					  telefone=data.get('telefone'),
					  tipo_perfil=data.get('tipo_perfil'))

		try:
			perfil.save()
			return HttpResponse("Cadastrado")
		except:
			pass
		return HttpResponse("Nao cadastrou")
