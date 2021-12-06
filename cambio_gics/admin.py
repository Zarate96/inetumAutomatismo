from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# REGISTRO DE IMPORTACIONES
class CambioGicsResource(resources.ModelResource):
    class meta:
        model=(Dalia)


@admin.register(Dalia)
class DaliaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = CambioGicsResource
    readonly_fields = ('created', 'updated')
    list_display = ('name','fecha', 'horario', 'om' ,'created', 'updated',)
    search_fields = ('name','created', 'updated',)

@admin.register(Notificacion_ti)
class Notificacion_tiProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = CambioGicsResource
    readonly_fields = ('created', 'updated')
    list_display = ( 'om' ,'titulo','fecha_inicio','hora_inicio', 'fecha_fin','hora_fin')
    search_fields = ( 'om' ,'titulo','fecha_inicio','hora_inicio','fecha_fin','hora_fin')

@admin.register(Notificacion_red)
class Notificacion_redProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = CambioGicsResource
    readonly_fields = ('created', 'updated')
    list_display = ( 'om' ,'titulo','fecha_inicio','hora_inicio','fecha_fin','hora_fin')
    search_fields = ( 'om' ,'titulo','fecha_inicio','hora_inicio','fecha_fin','hora_fin')