# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Assinatura(models.Model):
    id_plano = models.ForeignKey('Plano', models.DO_NOTHING, db_column='id_plano', blank=True, null=True)
    id_pagseguro = models.CharField(max_length=500, blank=True, null=True)
    data_assi = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assinatura'


class Aula(models.Model):
    id_modulo = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='id_modulo', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    url_aula = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aula'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Curso(models.Model):
    id_perfil = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Documento(models.Model):
    id_aula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='id_aula', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    url_arquivo = models.CharField(max_length=500, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documento'


class Duvida(models.Model):
    id_aula = models.ForeignKey(Aula, models.DO_NOTHING, db_column='id_aula', blank=True, null=True)
    titulo = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=750, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
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
        managed = False
        db_table = 'endereco'


class Modulo(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo'


class Perfil(models.Model):
    id_endereco = models.ForeignKey(Endereco, models.DO_NOTHING, db_column='id_endereco', blank=True, null=True)
    nome = models.CharField(max_length=350, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    email = models.CharField(max_length=350, blank=True, null=True)
    data_nasc = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    tipo_perfil = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'perfil'


class PerfilAssinatura(models.Model):
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil', blank=True, null=True)
    id_assinatura = models.ForeignKey(Assinatura, models.DO_NOTHING, db_column='id_assinatura', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil_assinatura'


class Plano(models.Model):
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_pagseguro = models.CharField(max_length=500, blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    periodo = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plano'


class Resposta(models.Model):
    id_duvida = models.ForeignKey(Duvida, models.DO_NOTHING, db_column='id_duvida', blank=True, null=True)
    descricao = models.CharField(max_length=750, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resposta'


class Situacao(models.Model):
    id_assinatura = models.ForeignKey(Assinatura, models.DO_NOTHING, db_column='id_assinatura', blank=True, null=True)
    descricao = models.CharField(max_length=500, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'situacao'
