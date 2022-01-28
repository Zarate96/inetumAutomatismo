from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(EstatusInterATT)
class CambioProject(admin.ModelAdmin):
    list_display = ('macno_centro_bundle_ether_300_estatus',)

@admin.register(RutasInterEstatus)
class RutasInterEstatusProject(admin.ModelAdmin):
    list_display = ('altan_vsbg2_tlane_estatus',)

@admin.register(RutasInterComentarios)
class RutasInterComentariosProject(admin.ModelAdmin):
    list_display = ('altan_vsbg2_tlane_comentarios',)

@admin.register(RutasInterFolioGuio)
class RutasInterFolioGuioProject(admin.ModelAdmin):
    list_display = ('altan_vsbg2_tlane_folios',)


@admin.register(HcAPN)
class HcAPN(admin.ModelAdmin):
    list_display = ('apn_mvn0_helppy_status',)