from django.db import models
from django.contrib.auth.models import User
import os
import phonenumbers
from django.conf import settings
from django.utils import timezone

class Usuario(models.Model):
    email = models.EmailField(max_length=100)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    contato = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome




class GeneroLivro(models.Model):
    nomeGenero = models.CharField(max_length=50)
    def __str__(self):
        return self.nomeGenero

class Livro(models.Model):
    OPÇÕES = (
        ('venda', 'Venda'),
        ('troca', 'Troca'),
        ('doacao', 'Doação'),
    )
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    tipo_transacao = models.CharField(max_length=10, choices=OPÇÕES, default='doacao')
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sinopse = models.TextField(blank=True, null=True)
    genero = models.ManyToManyField(GeneroLivro)
    whatsapp = models.CharField(help_text="DDD + Número", max_length=20, blank=True, null=True)
    capa = models.ImageField(upload_to='static/img/capas/', blank=True, null=True)
    usuario_email = models.EmailField(blank=True, null=True),
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data_exclusao = models.DateTimeField(null=True, blank=True)

    def excluir_completo(self):
        # Exclua o arquivo de capa associado ao livro se existir
        if self.capa:
            if os.path.isfile(self.capa.path):
                os.remove(self.capa.path)

        # Registre a data e hora da exclusão
        self.data_exclusao = timezone.now()
        self.save()

        # Agora você pode excluir o livro do banco de dados
        self.delete()

    

    def validar_e_formatar_numero(self):
        if self.whatsapp:
            try:
                whatsapp_obj = phonenumbers.parse("+55"+self.whatsapp, None)
                if phonenumbers.is_valid_number(whatsapp_obj):
                    # Formatar o número de telefone no formato internacional (por exemplo, +1 650-253-0000)
                    return phonenumbers.format_number(whatsapp_obj, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                else:
                    return "Número de telefone inválido."
            except phonenumbers.NumberParseException:
                return "Erro ao validar o número de telefone."
        else:
            return "Número de telefone não fornecido."

    def clean(self):
        if self.tipo_transacao in ['doacao', 'troca']:
            self.preco = None

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.capa}"
    
    def save(self, *args, **kwargs):
        if self.id:
            objeto_existente = Livro.objects.get(id=self.id)
            if objeto_existente.capa:
                if os.path.isfile(objeto_existente.capa.path):
                    os.remove(objeto_existente.capa.path)

        super(Livro, self).save(*args, **kwargs)


