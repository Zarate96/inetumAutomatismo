from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# REGISTRO DE IMPORTACIONES
class PerformanceResource(resources.ModelResource):
    class meta:
        model=(Categoria, SubCategoria , Performance)


@admin.register(Categoria)
class CategoriaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated',)
    search_fields = ('name','created', 'updated',)


@admin.register(SubCategoria)
class SubCategoriaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated',)
    search_fields = ('name', 'created', 'updated',)


@admin.register(Performance)
class PerformanceProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = PerformanceResource
    readonly_fields = ('created', 'updated')
    list_display = ('categoria', 'subcategoria', 'fecha','cantidad')
    list_filter = ('fecha','subcategoria', 'categoria')

##################################################################################################
