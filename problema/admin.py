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
    list_display = ('name','created','updated',)
    search_fields = ('name','created','updated',)


@admin.register(Catalogo)
class CatalogoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'id_soc', 'elemento_soc', 'ip_soc' , 'ambiente', 'tecnologia','get_proyecto')
    search_fields = ('name', 'id_soc', 'elemento_soc', 'ambiente', 'tecnologia__id',)

    def get_proyecto(self, obj):
        proyectos = Gestion.objects.filter(catalogo=obj.pk).order_by("created")
        lista =[]

        for proyecto in proyectos:
            lista.append(proyecto.id_proyecto)
            lista.append(proyecto.name_proyecto)
        return lista

    get_proyecto.short_description = "Proyectos"

@admin.register(Entregable)
class EntregableProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('estatus','name', 'compromiso','gestion')
    search_fields = ('name', 'compromiso','gestion__name_proyecto')
    list_filter = ('compromiso', 'estatus','gestion')


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
    list_display = ('name', 'area', 'apellido', 'telefono', 'email', 'created', 'updated')
    search_fields = ('name', 'area', 'apellido', 'telefono', 'email', 'created', 'updated')
    #list_filter = ('get_gerente__name', 'get_gerente__apellido')


@admin.register(GerenciaTemm)
class GerenciaTemmProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'apellido', 'telefono', 'email', 'created', 'updated')
    search_fields = ('name', 'apellido', 'telefono', 'email', 'created', 'updated')
    #list_filter = ('get_gerente__name', 'get_gerente__apellido')


@admin.register(Gestor)
class GestorProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'apellido', 'mrn', 'telefono', 'email', 'created', 'updated')
    search_fields = ('name', 'apellido', 'mrn', 'telefono', 'email', 'created', 'updated')
    list_filter = ('name',)


@admin.register(Grupo)
class GrupoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'elemento_soc', 'id_grupo', 'alta_workflow','get_proyecto')
    search_fields = ('name','elemento_soc__name')
    list_filter = ('name','elemento_soc__name') 
    ordering = ['created']

    def get_proyecto(self, obj):
        proyectos = Gestion.objects.filter(grupo=obj.pk).order_by("created")
        lista =[]

        for proyecto in proyectos:
            lista.append(proyecto.id_proyecto)
            lista.append(proyecto.name_proyecto)
        return lista
    
    get_proyecto.short_description = "Proyectos"

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
    list_display = ('name', 'area', 'apellido', 'telefono' ,'email' ,'gerente', 'created', 'updated')
    search_fields = ('name', 'area', 'apellido', 'telefono' ,'email' , 'created', 'updated')
    list_filter = ('gerente__name', 'gerente__apellido', 'gerente__telefono',)



@admin.register(LiderTecnicoTemm)
class LiderTecnicoTemmProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'apellido', 'telefono', 'email', 'gerente', 'created', 'updated')
    search_fields = ('name', 'apellido', 'telefono', 'email', 'created', 'updated')
    list_filter = ('gerente__name', 'gerente__apellido', 'gerente__telefono',)



@admin.register(Gestion)
class GestionProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('id_proyecto', 'name_proyecto', 'tipoProyecto', 'estatus', 'sub_estado', 'liberado', 'produccion', 'gestor',
                    'get_fechasEntregado','get_fechasNoEntregado','problema_catalogo',)
    search_fields = ('name_proyecto','tipoProyecto__name','estatus__name','gestor__name')
    raw_id_fields = ('grupo','catalogo','ot')

    def problema_catalogo(self, obj):
        return ", ".join(
            [c.name for c in obj.catalogo.all().order_by("name")])

    problema_catalogo.short_description = "Catalogos"

    def get_fechasEntregado(self, obj):
        entregables =  Entregable.objects.filter(gestion_id=obj.pk).order_by("created").filter(estatus=True)
        lista =[]

        for entregable in entregables:
            lista.append(entregable.name)
            lista.append(entregable.compromiso)
        return lista

        #return " / ".join(
        #    [str(c.compromiso) for c in Entregable.objects.filter(gestion_id=obj.pk).order_by("created")])

    get_fechasEntregado.short_description = "Entregables entregados"

    def get_fechasNoEntregado(self, obj):
        entregables =  Entregable.objects.filter(gestion_id=obj.pk).order_by("created").filter(estatus=False)
        lista =[]

        for entregable in entregables:
            lista.append(entregable.name)
            lista.append(entregable.compromiso)
        return lista

        #return " / ".join(
        #    [str(c.compromiso) for c in Entregable.objects.filter(gestion_id=obj.pk).order_by("created")])

    get_fechasNoEntregado.short_description = "Entregables no entregados"

@admin.register(Historico)
class HistoricoProject(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = ProblemaResource
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'compromiso','gestion')
    search_fields = ('name', 'compromiso',)
    list_filter = ('compromiso', )