# Generated by Django 3.2.7 on 2021-10-26 03:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_auto_20211015_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estatus',
            name='adicionales',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Comentarios Adicionales'),
        ),
    ]