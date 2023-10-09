from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import LivroForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse


from .models import *

def sobre(request):
    return render(request, 'homeAbout.html')

def livros(request):
    dados = Livro.objects.all()

    itens_por_pagina = 5
    paginator = Paginator(dados, itens_por_pagina)

    pagina = request.GET.get('pagina')
    dados_paginados = paginator.get_page(pagina)

    return render(request, 'todos.html', {'dados_paginados': dados_paginados})




def troca(request):
    dados = Livro.objects.filter(tipo_transacao='troca')

   
    itens_por_pagina = 5
    paginator = Paginator(dados, itens_por_pagina)

    pagina = request.GET.get('pagina')
    dados_paginados = paginator.get_page(pagina)

    return render(request, 'troca.html', {'dados_paginados': dados_paginados})


def venda(request):
    dados = Livro.objects.filter(tipo_transacao='venda')

    itens_por_pagina = 5
    paginator = Paginator(dados, itens_por_pagina)
    pagina = request.GET.get('pagina')
    dados_paginados = paginator.get_page(pagina)

    return render(request, 'venda.html', {'dados_paginados': dados_paginados})

def doacao(request):
    dados = Livro.objects.filter(tipo_transacao='doacao')

    itens_por_pagina = 5
    paginator = Paginator(dados, itens_por_pagina)

    pagina = request.GET.get('pagina')
    dados_paginados = paginator.get_page(pagina)

    return render(request, 'doacao.html', {'dados_paginados': dados_paginados})

def solicitaLivroEmail(request):
    send_mail('Assunto', 'Este é o email', 'arthursilvasouza98@hotmail.com', ['arthursilvasouza98@gmail.com'])
    return HttpResponse("Olá")

@login_required
def profile(request):
    livros_do_usuario = Livro.objects.filter(usuario=request.user)
    itens_por_pagina = 5
    paginator = Paginator(livros_do_usuario, itens_por_pagina)
    numero_pagina = request.GET.get('pagina')
    livros_paginados = paginator.get_page(numero_pagina)
    
    return render(request, 'profile.html', {'livros_do_usuario': livros_paginados})
    

@login_required
def cadLivro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            livro = form.save(commit=False)

            livro.usuario = request.user

            livro.save()
            return redirect('books')  
    else:
        form = LivroForm()
    return render(request, 'cadastLivros.html', {'form': form})

@login_required
def deletar_livros(request, pk):
    dado = get_object_or_404(Livro, pk=pk)
    
   
    if request.user == dado.usuario:
        dado.delete()
        
    else:
       
        pass


@login_required
def excluir_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if livro.capa:
        if os.path.isfile(livro.capa.path):
            os.remove(livro.capa.path)

    livro.delete()

    return JsonResponse({'message': 'Livro excluído com sucesso!'})