# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Aluno(models.Model):
    id_endereco = models.ForeignKey('Endereco', models.DO_NOTHING, db_column='id_endereco', blank=True, null=True)
    nome = models.CharField(max_length=350, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=350, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aluno'


class AlunoAssinatura(models.Model):
    id_aluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='id_aluno', blank=True, null=True)
    id_assinatura = models.ForeignKey('Assinatura', models.DO_NOTHING, db_column='id_assinatura', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aluno_assinatura'


class Assinatura(models.Model):
    id_plano = models.ForeignKey('Plano', models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    id_pagseguro = models.CharField(max_length=500, blank=True, null=True)
    data_assi = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assinatura'


class Aula(models.Model):
    id_modulo = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='id_modulo', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    url_aula = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'aula'


class Curso(models.Model):
    id_professor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='id_professor', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'curso'


class Documento(models.Model):
    id_aula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='id_aula', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    url_arquivo = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'documento'


class Duvida(models.Model):
    id_aula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='id_aula', blank=True, null=True)
    titulo = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=750, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

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
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modulo'


class Plano(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_pagseguro = models.CharField(max_length=500, blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    periodo = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plano'


class Professor(models.Model):
    id_endereco = models.ForeignKey(Endereco, models.DO_NOTHING, db_column='id_endereco', blank=True, null=True)
    nome = models.CharField(max_length=350, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'professor'


class Resposta(models.Model):
    id_duvida = models.ForeignKey(Duvida, models.DO_NOTHING, db_column='id_duvida', blank=True, null=True)
    descricao = models.CharField(max_length=750, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resposta'


class Situacao(models.Model):
    id_assinatura = models.ForeignKey(Assinatura, models.DO_NOTHING, db_column='id_assinatura', blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'situacao'
