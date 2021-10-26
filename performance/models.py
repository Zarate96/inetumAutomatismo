from django.db import models
from ckeditor.fields import RichTextField
from .tasks import notificacion_correo_rechado, notificacion_correo_aceptado

from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.
TIPO_ENLACE = (
    ('Principal', 'Principal'),
    ('Backup', 'Backup'),
)

NOMBRE = (
    ('ENTREGADO', 'ENTREGADO'),
    ('RECHAZADO', 'RECHAZADO'),
    ('ACEPTADO', 'ACEPTADO'),
)

REGION = (
    ('R1', 'R1'),
    ('R2', 'R2'),
    ('R3', 'R3'),
    ('R4', 'R4'),
    ('R5', 'R5'),
    ('R6', 'R6'),
    ('R7', 'R7'),
    ('R8', 'R8'),
    ('R9', 'R9'),
    ('TGS', 'TGS'),

)

MOTIVO = (
    ('FALTA DE INFORMACION', 'FALTA DE INFORMACION'),
    ('ERROR EN LA DOCUMENTACION', 'ERROR EN LA DOCUMENTACION'),
)


class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la SubCategoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categoria"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Servicio(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Servicio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Troncal(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre Troncal IPO")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Troncal"
        verbose_name_plural = "Troncales"
        ordering = ('created',)

    def __str__(self):
        return self.name

class Ingeniero(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ingeniero que Entrega")
    mail = models.EmailField(max_length=100, verbose_name="Correo", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Ingeniero"
        verbose_name_plural = "Ingenieros"
        ordering = ('created',)

    def __str__(self):
        return self.name




class Performance(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Cliente",blank=True, null=True)
    sucursal = models.CharField(max_length=100, verbose_name="Sucursal",blank=True, null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name="get_servicio",
                             verbose_name="Servicio",blank=True, null=True)

    troncal = models.ForeignKey(Troncal, on_delete=models.CASCADE, related_name="get_troncal",
                                 verbose_name="Troncal IPO",blank=True, null=True)

    tipo = models.CharField(choices=TIPO_ENLACE, max_length=45, verbose_name="Tipo Enlace",blank=True, null=True)

    identificador = models.CharField(max_length=100, verbose_name="OE-OI",blank=True, null=True)



    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="get_categoria",
                               verbose_name="Categoria", blank=True, null=True)

    region = models.CharField(choices=REGION, max_length=45, verbose_name="Región",blank=True, null=True)
    unico = models.CharField(max_length=100, verbose_name="ID UNICO",blank=True, null=True)
    regio = models.CharField(max_length=100, verbose_name="Codigo Regio",blank=True, null=True)
    ab = models.CharField(max_length=100, verbose_name="Ancho de Banda",blank=True, null=True)
    saltos = models.CharField(max_length=100, verbose_name="Saltos",blank=True, null=True)


    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gestor de Performance"
        verbose_name_plural = "Gestores de Performance"
        ordering = ('created',)

    def __str__(self):
        return str(self.categoria)

class Estatus(models.Model):
    name = models.CharField(choices=NOMBRE, max_length=45, verbose_name="Nombre")
    fecha = models.DateField(verbose_name="Fecha", blank=True, null=True)
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name="get_performance",
                                  verbose_name="Escoja la MT", blank=True, null=True)
    ingeniero = models.ForeignKey(Ingeniero, on_delete=models.CASCADE, related_name="get_ingeniero",
                                  verbose_name="Nombre del Ingeniero", blank=True, null=True)

    motivo = models.CharField(choices=MOTIVO, max_length=45, verbose_name="Motivo", blank=True, null=True)
    adicionales = RichTextField(verbose_name="Comentarios Adicionales", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Estatus"
        verbose_name_plural = "Estatus"
        ordering = ('created',)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if self.name == "RECHAZADO":
    #         notificacion_correo_rechado(self.name,self.performance.name, self.performance.sucursal,self.performance.identificador,self.motivo,self.ingeniero.name, self.ingeniero.mail)
    #         super().save(*args, **kwargs)


    #     elif self.name == "ACEPTADO":
    #         notificacion_correo_aceptado(self.name,self.performance.name, self.performance.sucursal,self.performance.identificador,self.ingeniero.name, self.ingeniero.mail)
    #         super().save(*args, **kwargs)

    #     else:
    #         super().save(*args, **kwargs)


#########################################################################################################



