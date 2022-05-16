from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# REGISTRO DE IMPORTACIONES
class GicsResource(resources.ModelResource):
    class meta:
        model=(Kpis_Fijos,General_Kpis_Fijos, Kpis_movil, General_Kpis_movil, Kpis_GRTC)


@admin.register(Kpis_Fijos)
class Kpis_Fijo_Project(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = GicsResource
    readonly_fields = ('created', 'updated')
    list_display = ('case_id','created', 'updated',)
    search_fields = ('case_id','created', 'updated',)



@admin.register(General_Kpis_Fijos)
class GeneralKpis_Fijo_Project(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = GicsResource
    #readonly_fields = ('created', 'updated')
    list_display = ('fecha',)
    search_fields = ('fecha',)


@admin.register(Kpis_movil)
class Kpis_Fijo_Project(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = GicsResource
    readonly_fields = ('created', 'updated')
    list_display = ('case_id','created', 'updated',)
    search_fields = ('case_id','created', 'updated',)



@admin.register(General_Kpis_movil)
class GeneralKpis_Movil_Project(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = GicsResource
    #readonly_fields = ('created', 'updated')
    list_display = ('fecha',)
    search_fields = ('fecha',)



@admin.register(Kpis_GRTC)
class Kpis_GRTC_Project(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = GicsResource
    readonly_fields = ('created', 'updated')
    list_display = ('folio',)
    search_fields = ('folio',)