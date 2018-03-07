#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
import requests
import json
import xml.etree.ElementTree as ET

# Create your views here.
@login_required
def cadastroaula(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'cadastroaula.html', {'logado':logado})

@login_required
def capivaraadm(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'adm_aprenda.html', {'logado':logado})

def index(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'site/index.html', {'logado':logado})

def login(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'site/login.html', {'logado':logado})

def detalhe_curso(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'site/detalhe_curso.html', {'logado':logado})

def lista_cursos(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'site/lista_cursos.html', {'logado':logado})

def area_aluno(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'site/area_aluno.html', {'logado':logado})

def aula_rep(request):
	logado = "nao"
	if request.user.is_authenticated():
		logado = "sim"
	return render(request, 'site/aula_rep.html', {'logado':logado})