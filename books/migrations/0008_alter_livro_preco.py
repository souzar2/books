# Generated by Django 4.2.5 on 2023-09-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_rename_preço_livro_preco_remove_livro_vender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='preco',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
