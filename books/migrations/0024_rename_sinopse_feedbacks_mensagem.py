# Generated by Django 4.2.5 on 2023-10-11 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_feedbacks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedbacks',
            old_name='sinopse',
            new_name='mensagem',
        ),
    ]
