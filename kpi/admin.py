from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# REGISTRO DE IMPORTACIONES
class KpisResource(resources.ModelResource):
    class meta:
        model=(Etapa, Estado, GestionProblema)

@admin.register(Estado)
class EstadoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = KpisResource
    readonly_fields = ('created', 'updated')
    list_display = ('name',)


@admin.register(Etapa)
class EtapaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = KpisResource
    readonly_fields = ('created', 'updated')
    list_display = ('name',)


@admin.register(GestionProblema)
class GestionProblemaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = KpisResource
    readonly_fields = ('created', 'updated')
    list_display = ('numero','titulo', 'registro',  'etapa', 'estado', 'proactivo' , 'postmortem', 'postmortem_acuse', 'minutas', 'problema', 'calidad', 'calidad_inventario', 'kedb')
