from django.contrib import admin
from .models import Medicamentos

class MedicamentosAdmin(admin.ModelAdmin):
    list_display = ("nome_generico", "nome_comercial", "quantidade")

admin.site.register(Medicamentos, MedicamentosAdmin)