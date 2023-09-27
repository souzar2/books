from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .models import *

def livros(request):

    livros = {
        'livros': Livro.objects.all()
    }

    return render(request, 'home.html', livros)



def troca(request):

    livros = {
        'livros': Livro.objects.all()
    }

    return render(request, 'troca.html', livros)


def venda(request):

    livros = {
        'livros': Livro.objects.all()
    }
    
    return render(request, 'venda.html', livros)

def doacao(request):

    livros = {
        'livros': Livro.objects.all()
    }

    return render(request, 'doacao.html', livros)

