from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# REGISTRO DE IMPORTACIONES
class PerformanceResource(resources.ModelResource):
    class meta:
        model=(Estatus, Categoria , Performance, Servicio, Troncal, Ingeniero)


@admin.register(Estatus)
class EstatusProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name','fecha', 'ingeniero',)
    search_fields = ('name','created', 'updated',)
    raw_id_fields = ('performance',)


@admin.register(Categoria)
class CategoriaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name', 'created', 'updated',)


@admin.register(Performance)
class PerformanceProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'sucursal','servicio', 'troncal', 'tipo','identificador', 'categoria','get_estatus', 'region',  'unico','regio', 'ab', 'saltos')
    list_filter = ( 'name','sucursal','identificador')
    search_fields = ('name','sucursal','identificador','categoria__name')


    def get_estatus(self, obj):
        estatus =  Estatus.objects.filter(performance__id=obj.pk).order_by("created")
        lista =[]

        for x in estatus:
            lista.append(x.name)
            lista.append(x.fecha)
        return lista

    get_estatus.short_description = "Estatus"

@admin.register(Servicio)
class ServicioriaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name', 'created', 'updated',)

@admin.register(Troncal)
class TroncalProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name', 'created', 'updated',)

@admin.register(Ingeniero)
class IngenieroProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name', 'created', 'updated',)



##################################################################################################
