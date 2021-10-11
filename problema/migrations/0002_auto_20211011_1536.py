# Generated by Django 3.2.7 on 2021-10-11 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problema', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gestion',
            options={'ordering': ('created',), 'verbose_name': 'Liberacion y despliegue', 'verbose_name_plural': 'Liberacion y despliegue'},
        ),
        migrations.AlterModelOptions(
            name='grupo',
            options={'ordering': ('created',), 'verbose_name': 'Elemento', 'verbose_name_plural': 'Elementos'},
        ),
        migrations.RemoveField(
            model_name='gerenciasoportetemm',
            name='mrn',
        ),
        migrations.RemoveField(
            model_name='gerenciatemm',
            name='mrn',
        ),
        migrations.RemoveField(
            model_name='lidertecnicotemm',
            name='mrn',
        ),
        migrations.RemoveField(
            model_name='soportetemm',
            name='mrn',
        ),
        migrations.AddField(
            model_name='entregable',
            name='estatus',
            field=models.BooleanField(default=False, verbose_name='Estatus'),
        ),
        migrations.AddField(
            model_name='gerenciasoportetemm',
            name='area',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre del area de soporte'),
        ),
        migrations.AddField(
            model_name='gerenciasoportetemm',
            name='telefono',
            field=models.CharField(default='', max_length=100, verbose_name='Numero de Telefono'),
        ),
        migrations.AddField(
            model_name='gerenciatemm',
            name='telefono',
            field=models.CharField(default='', max_length=100, verbose_name='Numero de Telefono'),
        ),
        migrations.AddField(
            model_name='gestion',
            name='comentarios',
            field=models.TextField(default='', verbose_name='Comentarios generales'),
        ),
        migrations.AddField(
            model_name='gestion',
            name='detencion',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Detencion de proyecto'),
        ),
        migrations.AddField(
            model_name='gestion',
            name='fecha_detencion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de detencion'),
        ),
        migrations.AddField(
            model_name='gestor',
            name='telefono',
            field=models.CharField(default='', max_length=100, verbose_name='Teléfono del Gestor'),
        ),
        migrations.AddField(
            model_name='lidertecnicotemm',
            name='telefono',
            field=models.CharField(default='', max_length=100, verbose_name='Numero de Telefono'),
        ),
        migrations.AddField(
            model_name='soportetemm',
            name='area',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre del area'),
        ),
        migrations.AddField(
            model_name='soportetemm',
            name='telefono',
            field=models.CharField(default='', max_length=100, verbose_name='Numero de Telefono'),
        ),
        migrations.AlterField(
            model_name='catalogo',
            name='ip_soc',
            field=models.GenericIPAddressField(blank=True, default=' ', null=True, verbose_name='Ip del SOC'),
        ),
        migrations.AlterField(
            model_name='catalogo',
            name='tecnologia',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_tecnologia_soc', to='problema.tecnologiacatalogo', verbose_name='Tecnología Soc'),
        ),
        migrations.AlterField(
            model_name='entregable',
            name='name',
            field=models.CharField(choices=[('KO', 'KO'), ('COMITÉ ARQ.', 'COMITÉ ARQ.'), ('PLAN PROYECTO', 'PLAN PROYECTO'), ('MINUTA KO', 'MINUTA KO'), ('SS', 'SS'), ('ALTA EN GESTORES', 'ALTA EN GESTORES'), ('RESPALDOS', 'RESPALDOS'), ('ESTADÍSTICAS', 'ESTADÍSTICAS'), ('LISTAS DE ALARMAS', 'LISTAS DE ALARMAS'), ('MT', 'MT'), ('ATP', 'ATP'), ('MO', 'MO'), ('SLA', 'SLA'), ('TOPOLOGÍA', 'TOPOLOGÍA'), ('CAPACITACIÓN', 'CAPACITACIÓN'), ('PRUEBAS CERTIFICACIÓN', 'PRUEBAS CERTIFICACIÓN'), ('CERTIFICADO SSL', 'CERTIFICADO SSL'), ('MANUALES', 'MANUALES'), ('RUTINAS O&M', 'RUTINAS O&M'), ('RM', 'RM'), ('DTS', 'DTS'), ('VOBO SOPORTE PRESUPUESTAL', 'VOBO SOPORTE PRESUPUESTAL'), ('OT FORMATO ABC', 'OT FORMATO ABC'), ('VOBO SOPORTE PARA PP', 'VOBO SOPORTE PARA PP'), ('ALTA DNS/PLANTILLAS', 'ALTA DNS/PLANTILLAS'), ('DIAGRAMA/ TOPOLOGIA KMZ', 'DIAGRAMA/ TOPOLOGIA KMZ'), ('REPORTE FOTOGRAFICO', 'REPORTE FOTOGRAFICO'), ('AE', 'AE'), ('AA', 'AA'), ('Otros', 'Otros')], max_length=200, verbose_name='Escoja el entregable'),
        ),
        migrations.AlterField(
            model_name='gestion',
            name='ot',
            field=models.ManyToManyField(default='N/A', related_name='get_ots', to='problema.Ot', verbose_name='Orden de Trabajo'),
        ),
        migrations.AlterField(
            model_name='gestion',
            name='sub_estado',
            field=models.CharField(blank=True, choices=[('Maqueta', 'Maqueta'), ('Servicio', 'Servicio'), ('Regularización', 'Regularización')], max_length=200, null=True, verbose_name='Sub-Estado'),
        ),
    ]
