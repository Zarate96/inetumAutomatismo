# Generated by Django 3.2.7 on 2021-11-30 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problema', '0012_alter_gestion_backlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregable',
            name='otros',
            field=models.BooleanField(blank=True, default='', help_text="Solo en caso de escoger 'Otros'", null=True, verbose_name='Especificar nombre'),
        ),
        migrations.AlterField(
            model_name='entregable',
            name='name',
            field=models.CharField(choices=[('GESTIÓN DE CUENTAS', 'GESTIÓN DE CUENTAS'), ('PRUEBAS DE REDUNDANCIA', 'PRUEBAS DE REDUNDANCIA'), ('KO', 'KO'), ('COMITÉ ARQ.', 'COMITÉ ARQ.'), ('PLAN PROYECTO', 'PLAN PROYECTO'), ('MINUTA KO', 'MINUTA KO'), ('SS', 'SS'), ('ALTA EN GESTORES', 'ALTA EN GESTORES'), ('RESPALDOS', 'RESPALDOS'), ('ESTADÍSTICAS', 'ESTADÍSTICAS'), ('LISTAS DE ALARMAS', 'LISTAS DE ALARMAS'), ('MT', 'MT'), ('ATP', 'ATP'), ('MO', 'MO'), ('SLA', 'SLA'), ('TOPOLOGÍA', 'TOPOLOGÍA'), ('CAPACITACIÓN', 'CAPACITACIÓN'), ('PRUEBAS CERTIFICACIÓN', 'PRUEBAS CERTIFICACIÓN'), ('CERTIFICADO SSL', 'CERTIFICADO SSL'), ('MANUALES', 'MANUALES'), ('RUTINAS O&M', 'RUTINAS O&M'), ('RM', 'RM'), ('DTS', 'DTS'), ('VOBO SOPORTE PRESUPUESTAL', 'VOBO SOPORTE PRESUPUESTAL'), ('OT FORMATO ABC', 'OT FORMATO ABC'), ('VOBO SOPORTE PARA PP', 'VOBO SOPORTE PARA PP'), ('ALTA DNS/PLANTILLAS', 'ALTA DNS/PLANTILLAS'), ('DIAGRAMA/ TOPOLOGIA KMZ', 'DIAGRAMA/ TOPOLOGIA KMZ'), ('REPORTE FOTOGRAFICO', 'REPORTE FOTOGRAFICO'), ('AE', 'AE'), ('AA', 'AA'), ('REVALIDACION SS', 'REVALIDACION SS'), ('REVALIDACION ALARMAS', 'REVALIDACION ALARMAS'), ('ACTUALIZACION DTS', 'ACTUALIZACION DTS'), ('CHECKLIST SO', 'CHECKLIST SO'), ('CHECKLIST BD', 'CHECKLIST BD'), ('Otros', 'Otros')], max_length=200, verbose_name='Escoja el entregable'),
        ),
        migrations.AlterField(
            model_name='historico',
            name='name',
            field=models.CharField(choices=[('GESTIÓN DE CUENTAS', 'GESTIÓN DE CUENTAS'), ('PRUEBAS DE REDUNDANCIA', 'PRUEBAS DE REDUNDANCIA'), ('KO', 'KO'), ('COMITÉ ARQ.', 'COMITÉ ARQ.'), ('PLAN PROYECTO', 'PLAN PROYECTO'), ('MINUTA KO', 'MINUTA KO'), ('SS', 'SS'), ('ALTA EN GESTORES', 'ALTA EN GESTORES'), ('RESPALDOS', 'RESPALDOS'), ('ESTADÍSTICAS', 'ESTADÍSTICAS'), ('LISTAS DE ALARMAS', 'LISTAS DE ALARMAS'), ('MT', 'MT'), ('ATP', 'ATP'), ('MO', 'MO'), ('SLA', 'SLA'), ('TOPOLOGÍA', 'TOPOLOGÍA'), ('CAPACITACIÓN', 'CAPACITACIÓN'), ('PRUEBAS CERTIFICACIÓN', 'PRUEBAS CERTIFICACIÓN'), ('CERTIFICADO SSL', 'CERTIFICADO SSL'), ('MANUALES', 'MANUALES'), ('RUTINAS O&M', 'RUTINAS O&M'), ('RM', 'RM'), ('DTS', 'DTS'), ('VOBO SOPORTE PRESUPUESTAL', 'VOBO SOPORTE PRESUPUESTAL'), ('OT FORMATO ABC', 'OT FORMATO ABC'), ('VOBO SOPORTE PARA PP', 'VOBO SOPORTE PARA PP'), ('ALTA DNS/PLANTILLAS', 'ALTA DNS/PLANTILLAS'), ('DIAGRAMA/ TOPOLOGIA KMZ', 'DIAGRAMA/ TOPOLOGIA KMZ'), ('REPORTE FOTOGRAFICO', 'REPORTE FOTOGRAFICO'), ('AE', 'AE'), ('AA', 'AA'), ('REVALIDACION SS', 'REVALIDACION SS'), ('REVALIDACION ALARMAS', 'REVALIDACION ALARMAS'), ('ACTUALIZACION DTS', 'ACTUALIZACION DTS'), ('CHECKLIST SO', 'CHECKLIST SO'), ('CHECKLIST BD', 'CHECKLIST BD'), ('Otros', 'Otros')], max_length=200, verbose_name='Escoja el entregable'),
        ),
    ]
