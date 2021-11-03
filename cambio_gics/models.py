from django.db import models

# Create your models here.

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