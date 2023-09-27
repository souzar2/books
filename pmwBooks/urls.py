
from django.contrib import admin
from django.urls import path
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.livros, name='books'),
    path('troca/', views.troca, name='troca'),
    path('venda/', views.venda, name='venda'),
    path('doacao/', views.doacao, name='doação'),
]
