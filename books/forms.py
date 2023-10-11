from django import forms
from .models import Livro, Feedbacks

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
            'capa': forms.FileInput(attrs={'class': 'form-control-file custom-file-input'}),
            'usuario': forms.HiddenInput(),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedbacks
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Deixe seu feedback aqui'}),
        }