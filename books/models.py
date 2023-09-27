from django.db import models
import os

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
    disponivel = models.BooleanField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sinopse = models.TextField()
    genero = models.ManyToManyField(GeneroLivro)
    capa = models.ImageField(upload_to='static/img/capas/')

    def clean(self):
        if self.tipo_transacao in ['doacao', 'troca']:
            self.preco = None

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.capa}"
    
    def save(self, *args, **kwargs):
        # Verifica se já existe uma imagem
        if self.id:
            objeto_existente = Livro.objects.get(id=self.id)
            if objeto_existente.capa:
                # Exclui a imagem existente do sistema de arquivos
                if os.path.isfile(objeto_existente.capa.path):
                    os.remove(objeto_existente.capa.path)
        super(Livro, self).save(*args, **kwargs)


