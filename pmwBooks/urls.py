
from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sobre , name='homeAbout'),
    path('todos', views.livros, name='books'),
    path('troca/', views.troca, name='troca'),
    path('venda/', views.venda, name='venda'),
    path('doacao/', views.doacao, name='doação'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('cadastroLivros/', views.cadLivro, name='cadastroLivro'),
    path('solicitaLivroEmail/', views.solicitaLivroEmail, name='solicitaLivro'),
    path('excluir-livro/<int:livro_id>/', views.excluir_livro, name='excluir_livro'),
]
