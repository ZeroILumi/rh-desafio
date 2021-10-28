from django.shortcuts import render, HttpResponse
from core.models import Company
from django.views.generic import TemplateView
from datetime import datetime

# Create your views here.

class Paginas(TemplateView):
    template_pagina_inicial = 'user_form.html'


def pagina_inicial(request):
    nome = 'Aruma tudo limitada'
    company = Company.objects.filter(name=nome)
    dados = {'companys': company}
    return render(request, Paginas.template_pagina_inicial, dados)
datetime.now().strftime('%d-%m-%Y')