# Generated by Django 3.2.7 on 2022-03-03 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problema', '0020_gestion_correo_seguimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestion',
            name='correo_seguimiento',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Correo de segumiento'),
        ),
    ]
