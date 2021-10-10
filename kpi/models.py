from django.db import models

# Create your models here.

class Etapa(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Etapa  del Proyecto"
        verbose_name_plural = "Etapas  del Proyecto"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Estado(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Estado del Folio"
        verbose_name_plural = "Estados de los Folios"
        ordering = ('created',)

    def __str__(self):
        return self.name


class GestionProblema(models.Model):
    numero = models.CharField(max_length=100, verbose_name="Número de FG")
    titulo = models.CharField(max_length=100, verbose_name="Titulo de FG")
    registro = models.BooleanField(verbose_name="Fue en Tiempo el Registro?", blank=True, null=True, default=False)

    etapa = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="get_etapas",
                             verbose_name="Etapa")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="get_estados",
                               verbose_name="Estado")
    proactivo = models.BooleanField(verbose_name="Proactivo?", blank=True, null=True, default=False)

    postmortem = models.BooleanField(verbose_name="Postmortem?", blank=True, null=True, default=False)
    postmortem_acuse = models.BooleanField(verbose_name="Se entrego en tiempo?", blank=True, null=True, default=False)
    minutas = models.BooleanField(verbose_name="Se entrego minutas?", blank=True, null=True, default=False)
    problema = models.BooleanField(verbose_name="Error en la Gestión?", blank=True, null=True, default=False)
    calidad = models.BooleanField(verbose_name="Calidad de Cierre?", blank=True, null=True, default=True)
    calidad_inventario = models.BooleanField(verbose_name="Calidad de Inventario?", blank=True, null=True, default=True)
    kedb = models.BooleanField(verbose_name="Reporte kedb?", blank=True, null=True, default=False)


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gestor de Problema"
        verbose_name_plural = "Gestores de Problemas"
        ordering = ('created',)
