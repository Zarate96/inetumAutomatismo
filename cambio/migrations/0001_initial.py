# Generated by Django 3.2.7 on 2022-04-11 23:08

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre del Area')),
                ('color_evento', colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Color de Fondo')),
                ('color_text', colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Color del Texto')),
                ('color_borde', colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='Color del Borde')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre de Categoria')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellido')),
                ('mail', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Teléfono')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_area', to='cambio.area', verbose_name='Area')),
            ],
            options={
                'verbose_name': 'Gerente',
                'verbose_name_plural': 'Gerentes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellido')),
                ('mail', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Teléfono')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Gestor',
                'verbose_name_plural': 'Gestores',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Planificada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Usuario Reviso')),
                ('fecha_solicitud', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Solicitud')),
                ('tarea', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Tarea')),
                ('titulo_tarea', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Titulo Tarea')),
                ('tipo_elemento', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Tipo de Elemento')),
                ('elemento', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Elemento')),
                ('tipo_trabajo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Tipo de Trabajo')),
                ('fecha_ejecucion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Ejecución')),
                ('area_asignada', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Area Asignada')),
                ('extraccion', models.BooleanField(blank=True, default=False, null=True, verbose_name='Se hizo la Extracción?')),
                ('area', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Area')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Cambio Planificado',
                'verbose_name_plural': 'Cambios  Planificados',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Promotor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellido')),
                ('mail', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Teléfono')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_gerente', to='cambio.gerente', verbose_name='Gerente')),
            ],
            options={
                'verbose_name': 'Promotor',
                'verbose_name_plural': 'Promotores',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre de Categoria')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_categpria', to='cambio.categoria', verbose_name='Area')),
            ],
            options={
                'verbose_name': 'Plataforma',
                'verbose_name_plural': 'Plataformas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='NoPlanificada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Titulo de la Actividad')),
                ('ot', models.CharField(max_length=1000, verbose_name='OT | |REQ | FG')),
                ('fecha', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y Hora solicitada')),
                ('plataforma', models.CharField(max_length=1000, verbose_name='Aplicación / Plataforma / Equipo')),
                ('areas', models.CharField(max_length=1000, verbose_name='Areas Involucradas')),
                ('detalle', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Detalle del Cambio')),
                ('beneficio', models.CharField(max_length=1000, verbose_name='Beneficios al negocio')),
                ('tiempo_ejecucion', models.TextField(blank=True, null=True, verbose_name='Tiempo de Ejecución')),
                ('tiempo_rollback', models.TextField(blank=True, null=True, verbose_name='Tiempo de Rollback')),
                ('tiempo_afectacion', models.TextField(blank=True, null=True, verbose_name='Tiempo de Afectación')),
                ('horario_afectacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='horario de Afectación')),
                ('servicio', models.CharField(max_length=1000, verbose_name='Servicios Afectados')),
                ('reinicio', models.CharField(max_length=1000, verbose_name='Indicar si el cambio requiere algún reinicio')),
                ('motivo', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Motivo de NO PLANIFICACIÓN')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
                ('promotor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_promotor', to='cambio.promotor', verbose_name='Promotor')),
            ],
            options={
                'verbose_name': 'Cambio NO planificado',
                'verbose_name_plural': 'Cambios NO planificados',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='GestionPlanificada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('om', models.CharField(blank=True, max_length=200, null=True, verbose_name='OM')),
                ('titulo', models.CharField(blank=True, max_length=2000, null=True, verbose_name='TITULO')),
                ('descripcion', models.TextField(blank=True, max_length=2000, null=True, verbose_name='DESCRIPCIÓN')),
                ('afectacion_b2b_b2c', models.CharField(blank=True, choices=[('B2B', 'B2B'), ('B2C', 'B2C'), ('N/A', 'N/A')], max_length=200, null=True, verbose_name='AFECTACIÓN (B2B o B2C)')),
                ('criticidad', models.CharField(blank=True, choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta'), ('Critical', 'Critical')], max_length=200, null=True, verbose_name='CRITICIDAD DEL CAMBIO')),
                ('impacto', models.CharField(blank=True, choices=[('Afectación', 'Afectación'), ('Riesgo', 'Riesgo'), ('N/A', 'N/A')], max_length=200, null=True, verbose_name='IMPACTO')),
                ('tiempo_ejecucion', models.DurationField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE EJECUCIÓN')),
                ('tiempo_rollback', models.DurationField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE ROLLBACK')),
                ('tiempo_afectacion', models.DurationField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE AFECTACION')),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True, verbose_name='FECHA INICIO')),
                ('fecha_fin', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='FECHA FIN')),
                ('afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='AFECTACIÓN')),
                ('horario', models.CharField(blank=True, max_length=200, null=True, verbose_name='HORARIO DE AFECTACIÓN')),
                ('area', models.CharField(blank=True, max_length=200, null=True, verbose_name='AREA')),
                ('comentarios', models.TextField(blank=True, null=True, verbose_name='COMENTARIOS EXTRAS')),
                ('comentarios_fechas', models.TextField(blank=True, null=True, verbose_name='COMENTARIOS SOBRE FECHAS')),
                ('motivo', models.TextField(blank=True, null=True, verbose_name='MOTIVO DEL RECHAZO')),
                ('aprobada_por_area', models.BooleanField(blank=True, default=False, null=True, verbose_name='APROBADA POR EL AREA')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_categoria', to='cambio.categoria', verbose_name='Categoria')),
                ('gerente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_gerente_red', to='cambio.gerente', verbose_name='Gerente')),
                ('gestor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_gestor', to='cambio.categoria', verbose_name='Gestor')),
            ],
            options={
                'verbose_name': 'Gestión Planificada',
                'verbose_name_plural': 'Gestión de las Planificadas',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='GestionNoPlanificada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=2000, null=True, verbose_name='TITULO')),
                ('descripcion', models.TextField(blank=True, max_length=2000, null=True, verbose_name='DESCRIPCIÓN')),
                ('afectacion_b2b_b2c', models.CharField(blank=True, choices=[('B2B', 'B2B'), ('B2C', 'B2C'), ('N/A', 'N/A')], max_length=200, null=True, verbose_name='AFECTACIÓN (B2B o B2C)')),
                ('criticidad', models.CharField(blank=True, choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta'), ('Critical', 'Critical')], max_length=200, null=True, verbose_name='CRITICIDAD DEL CAMBIO')),
                ('impacto', models.CharField(blank=True, choices=[('Afectación', 'Afectación'), ('Riesgo', 'Riesgo'), ('N/A', 'N/A')], max_length=200, null=True, verbose_name='IMPACTO')),
                ('tiempo_ejecucion', models.DurationField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE EJECUCIÓN')),
                ('tiempo_rollback', models.DurationField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE ROLLBACK')),
                ('tiempo_afectacion', models.DurationField(blank=True, max_length=200, null=True, verbose_name='TIEMPO DE AFECTACION')),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True, verbose_name='FECHA INICIO')),
                ('fecha_fin', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='FECHA FIN')),
                ('afectacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='AFECTACIÓN')),
                ('horario_inicio_afectacion', models.DateTimeField(blank=True, max_length=2000, null=True, verbose_name='HORARIO INICIO DE AFECTACION')),
                ('horario_entre_afectacion', models.DateTimeField(blank=True, max_length=200, null=True, verbose_name='HORARIO FIN AFECTACION')),
                ('area', models.CharField(blank=True, max_length=200, null=True, verbose_name='AREA')),
                ('fecha_inicio_propuesta', models.DateTimeField(blank=True, null=True, verbose_name='FECHA INICIO PROPUESTA')),
                ('fecha_fin_propuesta', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='FECHA FIN PROPUESTA')),
                ('motivo', models.TextField(blank=True, max_length=2000, null=True, verbose_name='MOTIVO DEL RECHAZO')),
                ('impacto_al_negocio', models.CharField(blank=True, max_length=2000, null=True, verbose_name='IMPACTO AL NEGECIO/OPERACIÓN')),
                ('motivo_no_planificado', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Motivo de NO PLANIFICACIÓN')),
                ('comentarios_fechas', models.TextField(blank=True, null=True, verbose_name='COMENTARIOS SOBRE FECHAS')),
                ('estatus_temm', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Estatus TEMM')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de edición')),
                ('gestor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_gestor_No_planificada', to='cambio.gestor', verbose_name='Gestor')),
                ('om', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_plataforma', to='cambio.noplanificada', verbose_name='OT')),
                ('plataforma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_plataforma', to='cambio.plataforma', verbose_name='Plataforma')),
            ],
            options={
                'verbose_name': 'Gestión No Planificada',
                'verbose_name_plural': 'Gestión de No Planificadas',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Nombre del Elemento')),
                ('fecha_hora_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de creación')),
                ('fecha_hora_fin', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de creación')),
                ('aprobado', models.BooleanField(blank=True, default=False, null=True, verbose_name='Tiene Ot aprobada?')),
                ('actividad', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Actividad')),
                ('gestion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_elemento', to='cambio.gestionnoplanificada', verbose_name='OT')),
                ('gestion_planificada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_elemento_planificada', to='cambio.gestionplanificada', verbose_name='OT Planificada')),
            ],
            options={
                'verbose_name': 'Elemento',
                'verbose_name_plural': 'Elementos',
            },
        ),
    ]
