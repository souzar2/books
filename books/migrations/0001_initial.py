# Generated by Django 4.2.5 on 2023-09-22 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneroLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeGenero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('contato', models.CharField(max_length=15)),
                ('cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('venderOuEmprestar', models.BooleanField()),
                ('disponivel', models.BooleanField()),
                ('preço', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sinopse', models.TextField()),
                ('capa', models.ImageField(upload_to='imgs/capas/')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.generolivro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.usuario')),
            ],
        ),
    ]
