# Generated by Django 3.2.7 on 2022-03-03 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problema', '0018_auto_20220223_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestion',
            name='palabra_clave',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Palabra clave'),
        ),
    ]
