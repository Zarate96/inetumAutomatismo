from .models import *
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class ProblemaResource(resources.ModelResource):
    class meta:
        model=(GestionNoPlanificada)

@admin.register(Notificacion)
class NotificacionProject(admin.ModelAdmin):
    readonly_fields = ('tiempo_ejecucion','created', 'updated', )
    list_display = ('om','created', 'updated')


@admin.register(Categoria)
class CategoriaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(Area)
class AreaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(Gerente)
class GerenteProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(Gestor)
class GestorProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')


@admin.register(Promotor)
class PromotorProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')



@admin.register(Elemento)
class ElementoProject(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(NoPlanificada)
class NoPlanificadaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('created', 'updated')


@admin.register(GestionNoPlanificada)
class GestionNoPlanificadaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated','area','tiempo_ejecucion')
    list_display = ('om','created', 'updated')
    list_filter = ('created','fecha_inicio')
    date_hierarchy = 'created'
    search_fields = ('created','om__ot')

