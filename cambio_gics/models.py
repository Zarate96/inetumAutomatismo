from django.db import models
from django.utils import  timezone
now = timezone.now

class Dalia(models.Model):
    numero = models.PositiveIntegerField(default=0, verbose_name="Numero del Ticket")
    fase = models.CharField(max_length=200, verbose_name="Fase Migración")
    regio = models.CharField(max_length=200, verbose_name="Regio")
    name = models.CharField(max_length=200, verbose_name="Nombre del Cliente")
    sucursal = models.CharField(max_length=200, verbose_name="Sucursal")
    fecha = models.DateField( verbose_name="Fecha de la Ventana",blank=True, null=True)
    horario = models.CharField(max_length=200, verbose_name="Horario",blank=True, null=True)
    om = models.CharField(max_length=200, verbose_name="Orden Maestra",blank=True, null=True)
    vlan = models.CharField(max_length=200, verbose_name="Vlan´s",blank=True, null=True)
    modelo = models.CharField(max_length=200, verbose_name="Modelo Cpe",blank=True, null=True)
    serie_cpe = models.CharField(max_length=200, verbose_name="Serie Cpe",blank=True, null=True)
    idcs = models.CharField(max_length=1000, verbose_name="Idcs",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Notificación Dalia"
        verbose_name_plural = "Notificaciones proyecto Dalia"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Notificacion_ti(models.Model):
    gerente = models.CharField(max_length=200, verbose_name="Gerente Responsable",blank=True, null=True)
    om = models.CharField(max_length=200, verbose_name="OM",blank=True, null=True)
    titulo = models.CharField(max_length=200, verbose_name="TITULO",blank=True, null=True)
    descripcion = models.TextField(max_length=1000, verbose_name="DESCRIPCIÓN",blank=True, null=True)
    afectacion = models.CharField(max_length=200, verbose_name="AFECTACIÓN (B2B o B2C)",blank=True, null=True)
    criticidad = models.CharField(max_length=200, verbose_name="CRITICIDAD DEL CAMBIO",blank=True, null=True)
    impacto = models.CharField(max_length=200, verbose_name="IMPACTO",blank=True, null=True)
    tiempo_ejecucion = models.CharField(max_length=200, verbose_name="TIEMPO DE EJECUCIÓN",blank=True, null=True)
    tiempo_rollback = models.CharField(max_length=200, verbose_name="TIEMPO DE ROLLBACK",blank=True, null=True)
    tiempo_afectacion = models.CharField(max_length=200, verbose_name="TIEMPO DE AFECTACION",blank=True, null=True)
    fecha_inicio = models.DateField(verbose_name="FECHA INICIO",  default=now,blank=True, null=True)
    hora_inicio = models.CharField(max_length=200,verbose_name="HORA INICIO",blank=True, null=True)

    fecha_fin = models.DateField(verbose_name="FECHA FIN", default=now,blank=True, null=True)
    hora_fin = models.CharField(max_length=200,verbose_name="HORA FIN",blank=True, null=True)
    detalle  = models.TextField(max_length=1000, verbose_name="AFECTACION",blank=True, null=True)
    horario_afectacion = models.CharField(max_length=200, verbose_name="HORARIO DE AFECTACION",blank=True, null=True)
    area =  models.CharField(max_length=200, verbose_name="ÁREA" ,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Notificación de TI"
        verbose_name_plural = "Notificaciones Actividades Criticas de TI"
        ordering = ('-created',)

class Notificacion_red(models.Model):
    gerente = models.CharField(max_length=200, verbose_name="Gerente Responsable",blank=True, null=True)
    categoria = models.CharField(max_length=200, verbose_name="CATEGORIA", blank=True, null=True)
    om = models.CharField(max_length=200, verbose_name="OM",blank=True, null=True)
    titulo = models.CharField(max_length=2000, verbose_name="TITULO",blank=True, null=True)
    descripcion = models.TextField(max_length=2000, verbose_name="DESCRIPCIÓN",blank=True, null=True)
    afectacion = models.CharField(max_length=200, verbose_name="AFECTACIÓN (B2B o B2C)",blank=True, null=True)
    criticidad = models.CharField(max_length=200, verbose_name="CRITICIDAD DEL CAMBIO",blank=True, null=True)
    impacto = models.CharField(max_length=200, verbose_name="IMPACTO",blank=True, null=True)
    tiempo_ejecucion = models.CharField(max_length=200, verbose_name="TIEMPO DE EJECUCIÓN",blank=True, null=True)
    tiempo_rollback = models.CharField(max_length=200, verbose_name="TIEMPO DE ROLLBACK",blank=True, null=True)
    tiempo_afectacion = models.CharField(max_length=200, verbose_name="TIEMPO DE AFECTACION",blank=True, null=True)
    fecha_inicio = models.DateField(verbose_name="FECHA INICIO",  default=now,blank=True, null=True)
    hora_inicio =models.CharField(max_length=200,verbose_name="HORA INICIO", blank=True, null=True)

    fecha_fin = models.DateField(verbose_name="FECHA FIN", default=now,blank=True, null=True)
    hora_fin = models.CharField(max_length=200,verbose_name="HORA FIN", blank=True, null=True)


    horario_afectacion = models.CharField(max_length=2000, verbose_name="HORARIO DE AFECTACION",blank=True, null=True)
    horario_entre_afectacion =  models.CharField(max_length=200, verbose_name="HORARIO ENTRE AFECTACION" ,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Notificación de RED"
        verbose_name_plural = "Notificaciones Actividades Criticas de RED"
        ordering = ('-created',)