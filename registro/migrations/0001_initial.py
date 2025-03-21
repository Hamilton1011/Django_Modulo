# Generated by Django 4.0.10 on 2025-03-08 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField(max_length=10)),
                ('lote', models.IntegerField(max_length=3)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]
