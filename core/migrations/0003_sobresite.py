# Generated by Django 5.2.1 on 2025-05-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_siteconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='SobreSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Sobre Nós', max_length=200, verbose_name='Título')),
                ('texto', models.TextField(blank=True, verbose_name='Texto')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='sobre/', verbose_name='Imagem da Loja')),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sobre o Site',
                'verbose_name_plural': 'Sobre o Site',
            },
        ),
    ]
