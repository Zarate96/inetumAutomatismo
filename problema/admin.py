from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# REGISTRO DE IMPORTACIONES
class ProblemaResource(resources.ModelResource):
    class meta:
        model=(Area,Catalogo,Entregable,Estatus,GerenciaSoporteTemm,GerenciaTemm,Gestor,Grupo,Ot,TecnologiaCatalogo,TipoProyecto,SoporteTemm,LiderTecnicoTemm,Gestion)


@admin.register(Area)
class AreaProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated',)
    search_fields = ('name','created', 'updated',)


@admin.register(Catalogo)
class CatalogoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'id_soc', 'elemento_soc', 'ip_soc' , 'ambiente', 'tecnologia',)
    search_fields = ('name', 'id_soc', 'elemento_soc', 'ip_soc' , 'ambiente', 'tecnologia',)
    list_filter = ('tecnologia',)


@admin.register(Entregable)
class EntregableProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'compromiso','grupo')
    search_fields = ('name', 'compromiso','grupo')
    list_filter = ('compromiso', 'grupo')


@admin.register(Estatus)
class EstatusProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')
    search_fields = ('name', 'created', 'updated')
    list_filter = ('get_estatus__id_proyecto', 'get_estatus__name_proyecto')


@admin.register(GerenciaSoporteTemm)
class GerenciaSoporteTemmProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'apellido', 'mrn', 'email', 'created', 'updated')
    search_fields = ('name', 'apellido', 'mrn', 'email', 'created', 'updated')
    list_filter = ('get_gerente__name', 'get_gerente__apellido')


@admin.register(GerenciaTemm)
class GerenciaTemmProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'apellido', 'mrn', 'email', 'created', 'updated')
    search_fields = ('name', 'apellido', 'mrn', 'email', 'created', 'updated')
    list_filter = ('get_gerente__name', 'get_gerente__apellido')


@admin.register(Gestor)
class GestorProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'apellido', 'mrn', 'email', 'created', 'updated')
    search_fields = ('name', 'apellido', 'mrn', 'email', 'created', 'updated')
    list_filter = ('name',)


@admin.register(Grupo)
class GrupoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'grupo', 'id_grupo', 'alta_workflow', 'get_entregable' )
    search_fields = ('name', 'grupo', 'id_grupo', 'alta_workflow',)
    list_filter = ('name', 'get_grupo',)
    ordering = ['created']

    def get_entregable(self, obj):
        return " / ".join(
            [c.name for c in Entregable.objects.filter(grupo_id=obj.pk).order_by("created")])


    get_entregable.short_description = "Entregables"


@admin.register(Ot)
class OtProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name','numero', 'elemento_soc', 'ejecucion', )
    search_fields = ('name','numero', 'elemento_soc', 'ejecucion' ,)
    list_filter = ('numero',)


@admin.register(TecnologiaCatalogo)
class TecnologiaCatalogoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    search_fields = ('name', 'created', 'updated')
    list_filter = ('name',)


@admin.register(TipoProyecto)
class TipoProyectoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    search_fields = ('name', 'created', 'updated')
    list_filter = ('name',)


@admin.register(SoporteTemm)
class SoporteTemmProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name','apellido', 'mrn' ,'email' ,'gerente', 'created', 'updated')
    search_fields = ('name','apellido', 'mrn' ,'email' , 'created', 'updated')
    list_filter = ('gerente__name', 'gerente__apellido', 'gerente__mrn',)



@admin.register(LiderTecnicoTemm)
class LiderTecnicoTemmProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'apellido', 'mrn', 'email', 'gerente', 'created', 'updated')
    search_fields = ('name', 'apellido', 'mrn', 'email', 'created', 'updated')
    list_filter = ('gerente__name', 'gerente__apellido', 'gerente__mrn',)



@admin.register(Gestion)
class GestionProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('id_proyecto', 'name_proyecto', 'tipoProyecto', 'estatus', 'sub_estado', 'liberado', 'produccion', 'gestor',
                    'kick_off','planificada','problema_catalogo', )
    search_fields = ('id_proyecto', 'name_proyecto', 'tipoProyecto', 'estatus', 'sub_estado', 'liberado', 'produccion', 'gestor',
                    'kick_off','planificada','problema_catalogo','grupo__name')
    raw_id_fields = ('grupo',)

    def problema_catalogo(self, obj):
        return ", ".join(
            [c.name for c in obj.catalogo.all().order_by("name")])

    problema_catalogo.short_description = "Catalogos"