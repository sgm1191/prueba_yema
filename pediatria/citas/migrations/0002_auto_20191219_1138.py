# Generated by Django 3.0.1 on 2019-12-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pediatra',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]