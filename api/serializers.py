from rest_framework import serializers
from website.models import *

class PerfilSerializer(serializers.ModelSerializer):

	endereco = serializers.SerializerMethodField('getendereco')

	class Meta:
		model = Perfil
		fields = ('id', 'endereco', 'nome', 'cpf', 'email', 'data_nasc', 'telefone', 'tipo_perfil')

	def getendereco(self, obj):
		serializer = EnderecoSerializer(obj.id_endereco)
		return serializer.data 

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'numero', 'bairro', 'cidade', 
        			'uf', 'pais', 'cep', 'complemento')

class CursoSerializer(serializers.ModelSerializer):
	
	perfil = serializers.SerializerMethodField('getperfil')

	class Meta:
		model = Curso
		fields = ('id', 'perfil', 'nome', 'descricao')
	
	def getperfil(self, obj):
		serializer = PerfilSerializer(obj.id_perfil)
		return serializer.data 

class ModuloSerializer(serializers.ModelSerializer):

	curso = serializers.SerializerMethodField('getcurso')	

	class Meta:
		model = Modulo
		fields = ('id', 'curso', 'nome', 'descricao')
	
	def getcurso(self, obj):
		serializer = CursoSerializer(obj.id_curso)
		return serializer.data		

class AulaSerializer(serializers.ModelSerializer):
	modulo = serializers.SerializerMethodField('getmodulo')	
	
	class Meta:
		model = Aula
		fields = ('id', 'modulo', 'nome', 'url_aula', 'descricao')
	
	def getmodulo(self, obj): 
		serializer = ModuloSerializer(obj.id_modulo)
		return serializer.data		


class DocumentoSerializer(serializers.ModelSerializer):

	aula = serializers.SerializerMethodField('getaula')

	class Meta:
		model = Documento
		fields = ('id', 'aula', 'nome', 'url_arquivo', 'descricao') 
	
	def getaula(self, obj):
		serializer = AulaSerializer(obj.id_aula)
		return serializer.data		

class DuvidaSerializer(serializers.ModelSerializer):
	
	aula = serializers.SerializerMethodField('getaula')

	class Meta:
		model = Duvida
		fields = ('id', 'aula', 'nome', 'descricao', 'data_criacao') 

	def getaula(self, obj):
		serializer = AulaSerializer(obj.id_aula)
		return serializer.data		

class RespostaSerializer(serializers.ModelSerializer):

	duvida = serializers.SerializerMethodField('getduvida')

	class Meta:
		model = Resposta
		fields = ('id', 'duvida', 'descricao', 'data_criacao')

	def getduvida(self, obj):
		serializer = DuvidaSerializer(obj.id_duvida)
		return serializer.data		

class PlanoSerializer(serializers.ModelSerializer):

	curso = serializers.SerializerMethodField('getcurso')	
	
	class Meta:
		model = Plano
		fields = ('id', 'curso', 'id_pagseguro', 'valor', 'periodo') 

	def getcurso(self, obj):
		serializer = CursoSerializer(obj.id_curso)
		return serializer.data	

class AssinaturaSerializer(serializers.ModelSerializer):
	
	plano = serializers.SerializerMethodField('getplano') 

	class Meta:
		model = Assinatura
		fields = ('id', 'plano', 'id_pagseguro', 'dat_assi') 

	def getplano(self, obj):
		serializer = PlanoSerializer(obj.id_plano)
		return serializer.data			

class SituacaoSerializer(serializers.ModelSerializer):
	
	assinatura = serializers.SerializerMethodField('getassinatura') 

	class Meta:
		model = Situacao
		fields = ('id', 'assinatura', 'descricao', 'data_criacao') 

	def getassinatura(self, obj):
		serializer = AssinaturaSerializer(obj.id_assinatura)
		return serializer.data					

class PerfilAssinaturaSerializer(serializers.ModelSerializer):

	perfil = serializers.SerializerMethodField('getperfil')	
	assinatura = serializers.SerializerMethodField('getassinatura') 	

	class Meta:
		model = PerfilAssinatura
		fields = ('id', 'perfil', 'assinatura')

	def getassinatura(self, obj):
		serializer = AssinaturaSerializer(obj.id_assinatura)
		return serializer.data

	def getperfil(self, obj):
		serializer = PerfilSerializer(obj.id_perfil)
		return serializer.data		