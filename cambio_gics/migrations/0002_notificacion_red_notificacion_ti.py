# Generated by Django 3.2.7 on 2021-12-06 19:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cambio_gics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion_red',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerente', models.CharField(blank=True, max_length=200, null=True, verbose_name='Gerente Responsable')),
                ('categoria', models.CharField(blank=True, max_length=200, null=True, verbose_name='CATEGORIA')),
                ('om', models.CharField(blank=True, max_length=200, null=True, verbose_name='OM')),
                ('titulo', models.CharField(blank=True, max_length=2000, null=True, verbose_name='TITULO')),
                ('descripcion', models.TextField(blank=True, max_length=2000, null=True, verbose_name='DESCRIPCIÓN')),
                ('afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='AFECTACIÓN (B2B o B2C)')),
                ('criticidad', models.CharField(blank=True, max_length=200, null=True, verbose_name='CRITICIDAD DEL CAMBIO')),
                ('impacto', models.CharField(blank=True, max_length=200, null=True, verbose_name='IMPACTO')),
                ('tiempo_ejecucion', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE EJECUCIÓN')),
                ('tiempo_rollback', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE ROLLBACK')),
                ('tiempo_afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE AFECTACION')),
                ('fecha_inicio', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='FECHA INICIO')),
                ('hora_inicio', models.CharField(blank=True, max_length=200, null=True, verbose_name='HORA INICIO')),
                ('fecha_fin', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='FECHA FIN')),
                ('hora_fin', models.CharField(blank=True, max_length=200, null=True, verbose_name='HORA FIN')),
                ('horario_afectacion', models.CharField(blank=True, max_length=2000, null=True, verbose_name='HORARIO DE AFECTACION')),
                ('horario_entre_afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='HORARIO ENTRE AFECTACION')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Notificación de RED',
                'verbose_name_plural': 'Notificaciones Actividades Criticas de RED',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Notificacion_ti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gerente', models.CharField(blank=True, max_length=200, null=True, verbose_name='Gerente Responsable')),
                ('om', models.CharField(blank=True, max_length=200, null=True, verbose_name='OM')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True, verbose_name='TITULO')),
                ('descripcion', models.TextField(blank=True, max_length=1000, null=True, verbose_name='DESCRIPCIÓN')),
                ('afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='AFECTACIÓN (B2B o B2C)')),
                ('criticidad', models.CharField(blank=True, max_length=200, null=True, verbose_name='CRITICIDAD DEL CAMBIO')),
                ('impacto', models.CharField(blank=True, max_length=200, null=True, verbose_name='IMPACTO')),
                ('tiempo_ejecucion', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE EJECUCIÓN')),
                ('tiempo_rollback', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE ROLLBACK')),
                ('tiempo_afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE AFECTACION')),
                ('fecha_inicio', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='FECHA INICIO')),
                ('hora_inicio', models.CharField(blank=True, max_length=200, null=True, verbose_name='HORA INICIO')),
                ('fecha_fin', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='FECHA FIN')),
                ('hora_fin', models.CharField(blank=True, max_length=200, null=True, verbose_name='HORA FIN')),
                ('detalle', models.TextField(blank=True, max_length=1000, null=True, verbose_name='AFECTACION')),
                ('horario_afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='HORARIO DE AFECTACION')),
                ('area', models.CharField(blank=True, max_length=200, null=True, verbose_name='ÁREA')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Notificación de TI',
                'verbose_name_plural': 'Notificaciones Actividades Criticas de TI',
                'ordering': ('-created',),
            },
        ),
    ]