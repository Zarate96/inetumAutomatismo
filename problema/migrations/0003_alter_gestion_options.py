# Generated by Django 3.2.7 on 2021-10-15 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problema', '0002_auto_20211011_1536'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gestion',
            options={'ordering': ('created',), 'verbose_name': 'Gestion de Proyectos', 'verbose_name_plural': 'Gestion de Proyectos'},
        ),
    ]