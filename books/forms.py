from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'tipo_transacao', 'whatsapp', 'preco', 'sinopse', 'genero', 'capa', 'usuario']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titulo'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DDD + Número'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço'}),
            'sinopse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sinopse(Opcional)'}),
            'genero': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': ''}),
            'usuario': forms.HiddenInput(),
        }