from django.contrib import admin
from .models import Institucion, Sede, CarreraOfertada, Representante


@admin.register(Institucion)
class InstitucionAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "ruc", "email", "activa", "fecha_registro")
    search_fields = ("nombre", "ruc", "email")
    list_filter = ("tipo", "activa")


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad", "telefono", "es_principal", "institucion")
    search_fields = ("nombre", "ciudad")
    list_filter = ("es_principal",)


@admin.register(CarreraOfertada)
class CarreraOfertadaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "institucion", "duracion_meses", "modalidad", "costo_anual")
    search_fields = ("nombre", "descripcion")
    list_filter = ("modalidad",)


@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ("usuario_id", "cargo", "es_principal", "institucion", "fecha_asignacion")
    search_fields = ("cargo", "usuario_id")
    list_filter = ("es_principal",)
