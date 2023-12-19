# Generated by Django 5.0 on 2023-12-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firma_adi', models.CharField(max_length=200, verbose_name='Firma Adı')),
                ('yetkili_adi', models.CharField(max_length=100, verbose_name='Yetkili Adı')),
                ('adres', models.TextField(verbose_name='Adres')),
                ('telefon_no', models.CharField(max_length=15, verbose_name='Telefon Numarası')),
                ('fax', models.CharField(blank=True, max_length=15, null=True, verbose_name='Faks')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail Adresi')),
            ],
        ),
    ]