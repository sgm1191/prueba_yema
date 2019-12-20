from django.contrib import admin
from .models import Pediatra, Paciente, Cita
from django.utils.translation import ugettext_lazy as _

# Register your models here.

class PediatraAdmin(admin.ModelAdmin):
    fields = ['nombre', 'apellido_paterno', 'apellido_materno']

class PacienteAdmin(admin.ModelAdmin):
    fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']

class CitaAdmin(admin.ModelAdmin):
    fields = ['fecha', 'hora', 'comentario', 'pediatra', 'paciente']

admin.site.register(Pediatra, PediatraAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cita, CitaAdmin)

admin.site.site_header = _("Prueba Yema Santiago Gonzalez")
admin.site.site_title = _("Prueba Yema Santiago Gonzalez")
admin.site.index_title = _("Bienvenido a la prueba de Yema - Santiago Gonzalez")