# Generated by Django 4.2.5 on 2023-10-04 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0016_alter_livro_capa_alter_livro_whatsapp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='usuario_email',
        ),
        migrations.AddField(
            model_name='livro',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
