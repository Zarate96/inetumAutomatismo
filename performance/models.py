from django.db import models

from django.dispatch import receiver
from django.db.models.signals import pre_save
# Create your models here.



class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ('created',)

    def __str__(self):
        return self.name

class SubCategoria(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la SubCategoria")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "SubCategoria"
        verbose_name_plural = "SubCategorias"
        ordering = ('created',)

    def __str__(self):
        return self.name


class Performance(models.Model):

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="get_categoria",
                             verbose_name="Categoría")

    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, related_name="get_estado",
                               verbose_name="Estado", blank=True, null=True)

    fecha = models.DateField( verbose_name="Fecha",blank=True, null=True)

    cantidad = models.PositiveIntegerField(default=0, verbose_name="Cantidad")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Gestor de Performance"
        verbose_name_plural = "Gestores de Performance"
        ordering = ('created',)

    def __str__(self):
        return str(self.categoria)
