# Generated by Django 4.1.7 on 2023-04-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_blogcreado_usuarioregistrado_delete_perfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcreado',
            name='tituloDelBlog',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuarioregistrado',
            name='nombreDeUsuario',
            field=models.CharField(max_length=20),
        ),
    ]