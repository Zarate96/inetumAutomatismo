# Generated by Django 3.2.7 on 2021-10-04 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Area de Ingeniería')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Area de Ingeniería',
                'verbose_name_plural': 'Areas de Ingenierías',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Hostname')),
                ('id_soc', models.PositiveIntegerField(default=0, verbose_name='ID del SOC')),
                ('elemento_soc', models.CharField(max_length=100, verbose_name='Elemento')),
                ('ip_soc', models.GenericIPAddressField(default=0, verbose_name='Ip del SOC')),
                ('ambiente', models.CharField(blank=True, choices=[('Pre-Producción', 'Pre-Producción'), ('Producción', 'Producción')], max_length=200, null=True, verbose_name='Ambiente SOC')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Catálogo',
                'verbose_name_plural': 'Catálogos',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Estatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Estatus')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Estatus',
                'verbose_name_plural': 'Estatus',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='GerenciaSoporteTemm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Gerente')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del Gerente')),
                ('mrn', models.CharField(max_length=100, verbose_name='MRN del Gerente')),
                ('email', models.EmailField(max_length=100, verbose_name='Email del Gerente')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Gerente Soporte de TEMM',
                'verbose_name_plural': 'Gerentes Soportes de TEMM',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='GerenciaTemm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Gerente')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del Gerente')),
                ('mrn', models.CharField(max_length=100, verbose_name='MRN del Gerente')),
                ('email', models.EmailField(max_length=100, verbose_name='Email del Gerente')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Gerente de TEMM',
                'verbose_name_plural': 'Gerentes de TEMM',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Gestor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Gestor')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del Gestor')),
                ('mrn', models.CharField(max_length=100, verbose_name='MRN del Gestor')),
                ('email', models.EmailField(max_length=100, verbose_name='Email del Gestor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Gestor Inetum',
                'verbose_name_plural': 'Gestores Inetum',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='TecnologiaCatalogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de Tecnología')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Tecnología',
                'verbose_name_plural': 'Tecnologías',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='TipoProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo de Proyecto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Tipo de Proyecto',
                'verbose_name_plural': 'Tipos de Proyectos',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='SoporteTemm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Sorpote')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del Soporte')),
                ('mrn', models.CharField(max_length=100, verbose_name='MRN del Soporte')),
                ('email', models.EmailField(max_length=100, verbose_name='Email del Soporte')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_gerente', to='problema.gerenciasoportetemm', verbose_name='Gerente del Proyecto')),
            ],
            options={
                'verbose_name': 'Soporte de TEMM',
                'verbose_name_plural': 'Soportes de TEMM',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Ot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Titulo de la Ot')),
                ('numero', models.PositiveIntegerField(default=0, verbose_name='Numero de la OT')),
                ('ejecucion', models.DateField(blank=True, null=True, verbose_name='Fecha de Ejecución de la OT')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('elemento_soc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_ot', to='problema.catalogo', verbose_name='Elemento')),
            ],
            options={
                'verbose_name': 'Orden de Trabajo',
                'verbose_name_plural': 'Ordenes de Trabajos',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='LiderTecnicoTemm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Lider')),
                ('apellido', models.CharField(max_length=100, verbose_name='Apellido del Lider')),
                ('mrn', models.CharField(max_length=100, verbose_name='MRN del Lider')),
                ('email', models.EmailField(max_length=100, verbose_name='Email del Lider')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_gerente', to='problema.gerenciatemm', verbose_name='Gerente del Proyecto')),
            ],
            options={
                'verbose_name': 'Lider Técnico de TEMM',
                'verbose_name_plural': 'Lideres Técnicos de TEMM',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del Elemento')),
                ('id_grupo', models.PositiveIntegerField(default=0, verbose_name='ID del Grupo')),
                ('alta_workflow', models.DateField(blank=True, null=True, verbose_name='Fecha de Alta WORKFLOW')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('elemento_soc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_grupo', to='problema.catalogo', verbose_name='Elemento')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_proyecto', models.PositiveIntegerField(default=0, verbose_name='ID del proyecto')),
                ('name_proyecto', models.CharField(max_length=100, verbose_name='Nombre del Proyecto')),
                ('sub_estado', models.CharField(blank=True, choices=[('Maqueta', 'Maqueta'), ('Servicio', 'Servicio')], max_length=200, null=True, verbose_name='Sub-Estado')),
                ('liberado', models.BooleanField(blank=True, default=False, null=True, verbose_name='Liberado por Temm')),
                ('produccion', models.BooleanField(blank=True, default=False, null=True, verbose_name='Puesto en Produccion')),
                ('kick_off', models.DateField(blank=True, null=True, verbose_name='Fecha Kick Off')),
                ('planificada', models.DateField(blank=True, null=True, verbose_name='Fecha Planificada')),
                ('pmo', models.CharField(max_length=100, verbose_name='Nombre del PMO')),
                ('impacto', models.BooleanField(blank=True, default=False, null=True, verbose_name='Impacto al Negocio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_area', to='problema.area', verbose_name='Area de Ingeniería')),
                ('catalogo', models.ManyToManyField(related_name='get_catalogo', to='problema.Catalogo', verbose_name='Catalogo')),
                ('estatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_estatus', to='problema.estatus', verbose_name='Estatus')),
                ('gestor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_gestor', to='problema.gestor', verbose_name='Gestor')),
                ('grupo', models.ManyToManyField(related_name='get_elementos', to='problema.Grupo', verbose_name='Grupos')),
                ('lider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_lider', to='problema.lidertecnicotemm', verbose_name='Lider Técnico')),
                ('ot', models.ManyToManyField(related_name='get_ots', to='problema.Ot', verbose_name='Orden de Trabajo')),
                ('soporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_soporte', to='problema.soportetemm', verbose_name='Soporte Técnico')),
                ('tipoProyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_tipo', to='problema.tipoproyecto', verbose_name='Tipo de Proyecto')),
            ],
            options={
                'verbose_name': 'Gestión de Proyecto',
                'verbose_name_plural': 'Gestión de Proyectos',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('KO', 'KO'), ('COMITÉ ARQ.', 'COMITÉ ARQ.'), ('PLAN PROYECTO', 'PLAN PROYECTO'), ('MINUTA KO', 'MINUTA KO'), ('SS', 'SS'), ('ALTA EN GESTORES', 'ALTA EN GESTORES'), ('RESPALDOS', 'RESPALDOS'), ('ESTADÍSTICAS', 'ESTADÍSTICAS'), ('LISTAS DE ALARMAS', 'LISTAS DE ALARMAS'), ('MT', 'MT'), ('ATP', 'ATP'), ('MO', 'MO'), ('SLA', 'SLA'), ('TOPOLOGÍA', 'TOPOLOGÍA'), ('CAPACITACIÓN', 'CAPACITACIÓN'), ('PRUEBAS CERTIFICACIÓN', 'PRUEBAS CERTIFICACIÓN'), ('CERTIFICADO SSL', 'CERTIFICADO SSL'), ('MANUALES', 'MANUALES'), ('RUTINAS O&M', 'RUTINAS O&M'), ('RM', 'RM'), ('DTS', 'DTS'), ('VOBO SOPORTE PRESUPUESTAL', 'VOBO SOPORTE PRESUPUESTAL'), ('OT FORMATO ABC', 'OT FORMATO ABC'), ('VOBO SOPORTE PARA PP', 'VOBO SOPORTE PARA PP'), ('ALTA DNS/PLANTILLAS', 'ALTA DNS/PLANTILLAS'), ('DIAGRAMA/ TOPOLOGIA KMZ', 'DIAGRAMA/ TOPOLOGIA KMZ'), ('REPORTE FOTOGRAFICO', 'REPORTE FOTOGRAFICO'), ('AE', 'AE'), ('AA', 'AA')], max_length=200, verbose_name='Escoja el entregable')),
                ('compromiso', models.DateField(blank=True, null=True, verbose_name='Fecha Compromiso del Entregable')),
                ('comentario', models.CharField(blank=True, max_length=100, null=True, verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('gestion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_gestion', to='problema.gestion', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Entregable',
                'verbose_name_plural': 'Entregables',
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='catalogo',
            name='tecnologia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_tecnologia_soc', to='problema.tecnologiacatalogo', verbose_name='Tecnología Soc'),
        ),
    ]