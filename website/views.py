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