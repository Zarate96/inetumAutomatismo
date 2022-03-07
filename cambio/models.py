from django.db import models
from django.utils import  timezone
from colorfield.fields import ColorField
from datetime import datetime, timedelta
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
import pandas as pd
import re
now = timezone.now

class Categoria(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre de Categoria", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Plataforma(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre de Categoria", blank=True, null=True)
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="get_categpria",
                      verbose_name="Area")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name



class Area(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre del Area", blank=True, null=True)
    color_evento = ColorField(verbose_name="Color de Fondo", blank=True, null=True)
    color_text = ColorField(verbose_name="Color del Texto", blank=True, null=True)
    color_borde = ColorField(verbose_name="Color del Borde", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Gerente(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    last_name = models.CharField(max_length=200, verbose_name="Apellido", blank=True, null=True)
    mail = models.EmailField(max_length=200, verbose_name="Correo", blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name="Teléfono", blank=True, null=True)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="get_area",
                                verbose_name="Area")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gerente"
        verbose_name_plural = "Gerentes"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Gestor(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    last_name = models.CharField(max_length=200, verbose_name="Apellido", blank=True, null=True)
    mail = models.EmailField(max_length=200, verbose_name="Correo", blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name="Teléfono", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gestor"
        verbose_name_plural = "Gestores"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Promotor(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    last_name = models.CharField(max_length=200, verbose_name="Apellido", blank=True, null=True)
    mail = models.EmailField(max_length=200, verbose_name="Correo", blank=True, null=True)
    phone = models.CharField(max_length=200, verbose_name="Teléfono", blank=True, null=True)
    gerente = models.ForeignKey(Gerente, on_delete=models.CASCADE, related_name="get_gerente",
                             verbose_name="Gerente")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Promotor"
        verbose_name_plural = "Promotores"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Notificacion(models.Model):
    CRITICIDAD = (
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
        ('Critical', 'Critical'),
    )

    IMPACTO = (
        ('Afectación', 'Afectación'),
        ('Riesgo', 'Riesgo'),
        ('N/A', 'N/A'),
    )

    AFECTACION = (
        ('B2B', 'B2B'),
        ('B2C', 'B2C'),
        ('N/A', 'N/A'),
    )

    gerente = models.ForeignKey(Gerente, on_delete=models.CASCADE, related_name="get_gerente_red",
                                verbose_name="Gerente")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="get_categoria",
                                verbose_name="Categoria")

    gestor = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="get_gestor",
                                  verbose_name="Gestor",blank=True, null=True)
    om = models.CharField(max_length=200, verbose_name="OM",blank=True, null=True)
    titulo = models.CharField(max_length=2000, verbose_name="TITULO",blank=True, null=True)
    descripcion = models.TextField(max_length=2000, verbose_name="DESCRIPCIÓN",blank=True, null=True)

    afectacion = models.CharField(choices=AFECTACION, max_length=200, verbose_name="AFECTACIÓN (B2B o B2C)",blank=True, null=True)
    criticidad = models.CharField(choices=CRITICIDAD, max_length=200, verbose_name="CRITICIDAD DEL CAMBIO",blank=True, null=True)
    impacto = models.CharField(choices=IMPACTO,max_length=200, verbose_name="IMPACTO",blank=True, null=True)

    tiempo_ejecucion = models.DurationField(max_length=200, verbose_name="TIEMPO DE EJECUCIÓN",blank=True, null=True)
    tiempo_rollback = models.DurationField(max_length=200, verbose_name="TIEMPO DE ROLLBACK",blank=True, null=True)
    tiempo_afectacion = models.DurationField(max_length=200, verbose_name="TIEMPO DE AFECTACION",blank=True, null=True)
    fecha_inicio = models.DateTimeField(verbose_name="FECHA INICIO",blank=True, null=True)
    fecha_fin = models.DateTimeField(verbose_name="FECHA FIN", default=now,blank=True, null=True)

    horario_inicio_afectacion = models.DateTimeField(max_length=2000, verbose_name="HORARIO INICIO DE AFECTACION",blank=True, null=True)
    horario_entre_afectacion =  models.DateTimeField(max_length=200, verbose_name="HORARIO FIN AFECTACION" ,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Planificada"
        verbose_name_plural = "Planificadas"
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        self.tiempo_ejecucion = self.fecha_fin - self.fecha_inicio
        super().save(*args, **kwargs)


class NoPlanificada(models.Model):
    titulo = models.CharField(max_length=1000, verbose_name="Titulo de la Actividad", blank=True, null=True)
    ot = models.CharField(max_length=1000, verbose_name="OT | |REQ | FG")
    fecha = models.DateTimeField(verbose_name="Fecha y Hora solicitada", blank=True, null=True)
    plataforma = models.CharField(max_length=1000, verbose_name="Aplicación / Plataforma / Equipo")
    areas = models.CharField(max_length=1000, verbose_name="Areas Involucradas")
    detalle = models.TextField(max_length=1000, verbose_name="Detalle del Cambio", blank=True, null=True)
    beneficio = models.CharField(max_length=1000, verbose_name="Beneficios al negocio")
    tiempo_ejecucion = models.TextField(verbose_name="Tiempo de Ejecución", blank=True, null=True)
    tiempo_rollback = models.TextField(verbose_name="Tiempo de Rollback", blank=True, null=True)
    tiempo_afectacion = models.TextField(verbose_name="Tiempo de Afectación", blank=True, null=True)
    horario_afectacion = models.CharField(max_length=100, verbose_name="horario de Afectación", blank=True, null=True)
    servicio = models.CharField(max_length=1000, verbose_name="Servicios Afectados")
    reinicio = models.CharField(max_length=1000, verbose_name="Indicar si el cambio requiere algún reinicio")
    promotor = models.ForeignKey(Promotor, on_delete=models.CASCADE, related_name="get_promotor",
                                  verbose_name="Promotor",blank=True, null=True)
    motivo = models.TextField(max_length=1000, verbose_name="Motivo de NO PLANIFICACIÓN",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación",null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True, blank=True)

    class Meta:
        verbose_name = "Cambio NO planificado"
        verbose_name_plural = "Cambios NO planificados"
        ordering = ["-created"]

    def __str__(self):
        return self.ot




class GestionNoPlanificada(models.Model):
    CRITICIDAD = (
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
        ('Critical', 'Critical'),
    )

    IMPACTO = (
        ('Afectación', 'Afectación'),
        ('Riesgo', 'Riesgo'),
        ('N/A', 'N/A'),
    )

    AFECTACION = (
        ('B2B', 'B2B'),
        ('B2C', 'B2C'),
        ('N/A', 'N/A'),
    )


    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name="get_plataforma",
                                verbose_name="Plataforma",blank=True, null=True)




    om =  models.ForeignKey(NoPlanificada, on_delete=models.CASCADE, related_name="get_plataforma",
                                verbose_name="OT",blank=True, null=True)



    titulo = models.CharField(max_length=2000, verbose_name="TITULO",blank=True, null=True)
    descripcion = models.TextField(max_length=2000, verbose_name="DESCRIPCIÓN",blank=True, null=True)

    afectacion_b2b_b2c = models.CharField(choices=AFECTACION, max_length=200, verbose_name="AFECTACIÓN (B2B o B2C)",blank=True, null=True)
    criticidad = models.CharField(choices=CRITICIDAD, max_length=200, verbose_name="CRITICIDAD DEL CAMBIO",blank=True, null=True)
    impacto = models.CharField(choices=IMPACTO,max_length=200, verbose_name="IMPACTO",blank=True, null=True)

    tiempo_ejecucion = models.DurationField(max_length=200, verbose_name="TIEMPO DE EJECUCIÓN",blank=True, null=True)
    tiempo_rollback = models.DurationField(max_length=200, verbose_name="TIEMPO DE ROLLBACK",blank=True, null=True)
    tiempo_afectacion = models.DurationField(max_length=200, verbose_name="TIEMPO DE AFECTACION",blank=True, null=True)

    fecha_inicio = models.DateTimeField(verbose_name="FECHA INICIO",blank=True, null=True)
    fecha_fin = models.DateTimeField(verbose_name="FECHA FIN", default=now,blank=True, null=True)
    afectacion= models.CharField( max_length=200, verbose_name="AFECTACIÓN",
                                          blank=True, null=True)

    horario_inicio_afectacion = models.DateTimeField(max_length=2000, verbose_name="HORARIO INICIO DE AFECTACION",blank=True, null=True)
    horario_entre_afectacion =  models.DateTimeField(max_length=200, verbose_name="HORARIO FIN AFECTACION" ,blank=True, null=True)

    area = models.CharField(max_length=200, verbose_name="AREA",
                                  blank=True, null=True)

    fecha_inicio_propuesta = models.DateTimeField(verbose_name="FECHA INICIO PROPUESTA", blank=True, null=True)
    fecha_fin_propuesta  = models.DateTimeField(verbose_name="FECHA FIN PROPUESTA", default=now, blank=True, null=True)

    motivo = models.TextField(max_length=2000, verbose_name="MOTIVO DEL RECHAZO", blank=True, null=True)

    impacto_al_negocio = models.CharField(max_length=2000, verbose_name="IMPACTO AL NEGECIO/OPERACIÓN", blank=True, null=True)

    motivo_no_planificado = models.CharField(max_length=2000, verbose_name="Motivo de NO PLANIFICACIÓN", blank=True,
                                          null=True)
    gestor = models.ForeignKey(Gestor, on_delete=models.CASCADE, related_name="get_gestor_No_planificada",
                               verbose_name="Gestor", blank=True, null=True)
    estatus_temm = models.CharField(max_length=2000, verbose_name="Estatus TEMM", blank=True,
                                             null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición", null=True, blank=True)

    class Meta:
        verbose_name = "Gestión No Planificada"
        verbose_name_plural = "Gestión de No Planificadas"
        ordering = ('-created',)

    def __str__(self):
        return self.om.ot

    def save(self, *args, **kwargs):
        if self.fecha_fin and self.fecha_inicio:
            self.tiempo_ejecucion = self.fecha_fin - self.fecha_inicio
            super().save(*args, **kwargs)

        if self.om.promotor:
            self.area = self.om.promotor.gerente.area.name
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)


class Elemento(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Elemento")
    fecha_hora_inicio = models.DateTimeField(verbose_name="Fecha de creación", null=True, blank=True)
    fecha_hora_fin = models.DateTimeField(verbose_name="Fecha de creación", null=True, blank=True)
    gestion = models.ForeignKey(GestionNoPlanificada, on_delete=models.CASCADE, related_name="get_elemento",
                                 verbose_name="OT", blank=True, null=True)
    aprobado = models.BooleanField(default=False, verbose_name="Tiene Ot aprobada?", blank=True, null=True)
    class Meta:
        verbose_name = "Elemento"
        verbose_name_plural = "Elementos"

    def __str__(self):
        return self.name


@receiver(post_save, sender=GestionNoPlanificada)
def validador(sender,instance, **kwargs):
    try:
        if not instance.motivo:
            flag_diario= True
            if instance.fecha_inicio:
                delta = instance.fecha_inicio - instance.created
                hours = delta.days * 24 + delta.seconds / 3600

                if hours < 48:
                    instance.motivo = f'Rechazada debido a que no cumple con las 48 horas.'
                    flag_diario = False

                else:
                    promotor = str(instance.om.promotor)
                    if (promotor == "Irving" or promotor == "Vianney") and instance.titulo:
                        patrones = ['[mM][aA][nN][dD][aA][tT][oO][rR][iI][aA]', '[Cc][Uu][Bb][Ii][Cc][Aa][Cc][Ii][Ooó][Nn]' ]

                        if len(re.findall(patrones[0], instance.titulo)) > 0:
                            flag_diario = True

                        elif len(re.findall(patrones[1], instance.titulo)) > 0:
                            flag_diario = True


                        else:
                            instance.motivo = 'Rechazada debido a que no Tiene la Palabra Mandatoria o Cubicación en el titulo.'
                            flag_diario = False


            elementos_propuestos = Elemento.objects.filter(gestion_id=instance.pk)
            if elementos_propuestos:
                for elemento_propuesto in elementos_propuestos:
                    fecha_propuesta = pd.Timestamp(elemento_propuesto.fecha_hora_inicio.date(),tz='America/Mexico_City')
                    fecha_p2 =elemento_propuesto.fecha_hora_inicio.date() +  timedelta(days=1)
                    fecha_propuesta2= pd.Timestamp(fecha_p2, tz='America/Mexico_City')

                    fecha_propuesta_inicio = pd.Timestamp(elemento_propuesto.fecha_hora_inicio).tz_convert('America/Mexico_City')
                    fecha_propuesta_fin = pd.Timestamp(elemento_propuesto.fecha_hora_fin).tz_convert('America/Mexico_City')

                    #Todas los elementos con OTs activos de ese dia.
                    elementos_activos = Elemento.objects.filter(name=elemento_propuesto.name).filter(fecha_hora_inicio__gte=fecha_propuesta).filter(fecha_hora_fin__lt=fecha_propuesta2).filter(aprobado=True).exclude(gestion_id=instance.pk).order_by('-fecha_hora_fin')

                    if elementos_activos and flag_diario :

                        delta =pd.date_range(start=fecha_propuesta_inicio, end=fecha_propuesta_fin,
                                      freq='30min').tz_convert('America/Mexico_City')

                        for x in elementos_activos:
                            fecha_inicio_activos = pd.Timestamp(x.fecha_hora_inicio).tz_convert('America/Mexico_City')
                            fecha_fin_activos= pd.Timestamp(x.fecha_hora_fin).tz_convert('America/Mexico_City')
                            delta2 = pd.date_range(start=fecha_inicio_activos, end=fecha_fin_activos,
                                      freq='30min').tz_convert('America/Mexico_City')
                            for z in delta2[:-1]:
                                if z in delta:

                                    instance.motivo = f'Rechazada debido a que el elemento {elemento_propuesto.name} no se encuentra disponible en la fecha y hora propuesta {z} ,solapa con la ot  {x.gestion.om.ot}.'
                                    instance.save()
                                    elemento_propuesto.aprobado = False
                                    elemento_propuesto.save()
                                    flag_diario = False
                                    break

                            if flag_diario:
                                elemento_propuesto.aprobado = True
                                elemento_propuesto.save()

                    else:
                        if flag_diario:
                            instance.motivo = 'REVISAR'
                            elemento_propuesto.aprobado = True
                            elemento_propuesto.save()

    except sender.DoesNotExist:
        pass