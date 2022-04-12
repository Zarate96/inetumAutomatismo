from .models import *
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ProblemaResource(resources.ModelResource):
    class meta:
        model=(Categoria,Area,Gerente,Gestor,Promotor,Elemento,NoPlanificada,GestionNoPlanificada,GestionPlanificada)

@admin.register(Categoria)
class CategoriaProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')

@admin.register(Area)
class AreaProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')

@admin.register(Gerente)
class GerenteProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')

@admin.register(Gestor)
class GestorProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')

@admin.register(Promotor)
class PromotorProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')

@admin.register(Elemento)
class ElementoProject(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)

@admin.register(NoPlanificada)
class NoPlanificadaProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('created', 'updated')

@admin.register(GestionNoPlanificada)
class GestionNoPlanificadaProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated','area','tiempo_ejecucion')
    list_display = ('om','created', 'updated')
    list_filter = ('created','fecha_inicio')
    date_hierarchy = 'created'
    search_fields = ('created','om__ot')

@admin.register(Planificada)
class PlanificadaProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('created', 'updated')

@admin.register(GestionPlanificada)
class GestionPlanificadaProject(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('om','created', 'updated')