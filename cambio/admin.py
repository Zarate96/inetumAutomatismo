from django.contrib import admin
from .models import *
# Register your models here.




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

@admin.register(Planificada)
class PlanificadaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('created', 'updated')

@admin.register(GestionPlanificada)
class GestionPlanificadaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('om','created', 'updated')