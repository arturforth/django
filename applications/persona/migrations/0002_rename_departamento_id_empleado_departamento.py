# Generated by Django 3.2 on 2021-04-20 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='departamento_id',
            new_name='departamento',
        ),
    ]
