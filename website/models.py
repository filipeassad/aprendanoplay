from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Assinatura(models.Model):
    id_plano = models.ForeignKey('Plano', db_column='id_plano', blank=True, null=True)
    id_pagseguro = models.CharField(max_length=500, blank=True, null=True)
    data_assi = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assinatura'

class Aula(models.Model):
    id_modulo = models.ForeignKey('Modulo', db_column='id_modulo', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    url_aula = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self): 
        return self.nome.encode('utf8') + (" - ").encode('utf8') + self.id_modulo.nome.encode('utf8') + (" - ").encode('utf8') + self.id_modulo.id_curso.nome.encode('utf8')  

    class Meta:
        managed = True
        db_table = 'aula'

class Curso(models.Model):
    id_perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self): 
        return self.nome.encode('utf8')

    class Meta:
        managed = True
        db_table = 'curso'

class Documento(models.Model):
    id_aula = models.ForeignKey('Aula', db_column='id_aula', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    url_arquivo = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self): 
        return self.nome.encode('utf8')

    class Meta:
        managed = True
        db_table = 'documento'

class Duvida(models.Model):
    id_aula = models.ForeignKey('Aula', db_column='id_aula', blank=True, null=True)
    titulo = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=750, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    def __str__(self): 
        return self.titulo.encode('utf8')

    class Meta:
        managed = True
        db_table = 'duvida'

class Endereco(models.Model):
    logradouro = models.CharField(max_length=350, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=250, blank=True, null=True)
    cidade = models.CharField(max_length=250, blank=True, null=True)
    uf = models.CharField(max_length=250, blank=True, null=True)
    pais = models.CharField(max_length=250, blank=True, null=True)
    cep = models.CharField(max_length=30, blank=True, null=True)
    complemento = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'endereco'

class Modulo(models.Model):
    id_curso = models.ForeignKey('Curso', db_column='id_curso', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self): 
        return self.nome.encode('utf8') + (" - ").encode('utf8') + self.id_curso.nome.encode('utf8')

    class Meta:
        managed = True
        db_table = 'modulo'

class Perfil(models.Model):
    id_endereco = models.ForeignKey(Endereco, models.DO_NOTHING, db_column='id_endereco', blank=True, null=True)
    nome = models.CharField(max_length=350, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=350, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    tipo_perfil = models.TextField(max_length=100, blank=True, null=True) 
    user = models.OneToOneField(User, related_name='profile')

    def __str__(self): 
        return self.nome.encode('utf8')

    class Meta:
        managed = True
        db_table = 'perfil'

class PerfilAssinatura(models.Model):
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    id_assinatura = models.ForeignKey(Assinatura, models.DO_NOTHING, db_column='id_assinatura', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'perfil_assinatura'

class Plano(models.Model):
    id_curso = models.ForeignKey('Curso', db_column='id_curso', blank=True, null=True)
    id_pagseguro = models.CharField(max_length=500, blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    periodo = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self): 
        return self.periodo.encode('utf8')

    class Meta:
        managed = True
        db_table = 'plano'

class Resposta(models.Model):
    id_duvida = models.ForeignKey('Duvida', db_column='id_duvida', blank=True, null=True)
    descricao = models.CharField(max_length=750, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resposta'

class Situacao(models.Model):
    id_assinatura = models.ForeignKey('Assinatura', db_column='id_assinatura', blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'situacao'

