
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
    path('accounts/', include('allauth.urls')),
]
