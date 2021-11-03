# Generated by Django 3.2.7 on 2021-11-03 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problema', '0005_auto_20211025_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('KO', 'KO'), ('COMITÉ ARQ.', 'COMITÉ ARQ.'), ('PLAN PROYECTO', 'PLAN PROYECTO'), ('MINUTA KO', 'MINUTA KO'), ('SS', 'SS'), ('ALTA EN GESTORES', 'ALTA EN GESTORES'), ('RESPALDOS', 'RESPALDOS'), ('ESTADÍSTICAS', 'ESTADÍSTICAS'), ('LISTAS DE ALARMAS', 'LISTAS DE ALARMAS'), ('MT', 'MT'), ('ATP', 'ATP'), ('MO', 'MO'), ('SLA', 'SLA'), ('TOPOLOGÍA', 'TOPOLOGÍA'), ('CAPACITACIÓN', 'CAPACITACIÓN'), ('PRUEBAS CERTIFICACIÓN', 'PRUEBAS CERTIFICACIÓN'), ('CERTIFICADO SSL', 'CERTIFICADO SSL'), ('MANUALES', 'MANUALES'), ('RUTINAS O&M', 'RUTINAS O&M'), ('RM', 'RM'), ('DTS', 'DTS'), ('VOBO SOPORTE PRESUPUESTAL', 'VOBO SOPORTE PRESUPUESTAL'), ('OT FORMATO ABC', 'OT FORMATO ABC'), ('VOBO SOPORTE PARA PP', 'VOBO SOPORTE PARA PP'), ('ALTA DNS/PLANTILLAS', 'ALTA DNS/PLANTILLAS'), ('DIAGRAMA/ TOPOLOGIA KMZ', 'DIAGRAMA/ TOPOLOGIA KMZ'), ('REPORTE FOTOGRAFICO', 'REPORTE FOTOGRAFICO'), ('AE', 'AE'), ('AA', 'AA'), ('Otros', 'Otros')], max_length=200, verbose_name='Escoja el entregable')),
                ('compromiso', models.DateField(blank=True, null=True, verbose_name='Fecha Compromiso del Entregable')),
                ('comentario', models.CharField(blank=True, max_length=100, null=True, verbose_name='Comentario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('gestion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_gestion_historico', to='problema.gestion')),
            ],
            options={
                'verbose_name': 'Historico',
                'verbose_name_plural': 'Historicos',
                'ordering': ('created',),
            },
        ),
    ]
