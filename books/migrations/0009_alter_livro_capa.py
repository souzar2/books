# Generated by Django 4.2.5 on 2023-09-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_livro_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.ImageField(upload_to='static/img/capas/'),
        ),
    ]
