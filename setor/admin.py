from django.contrib import admin
from .models import Setor

class SetorAdmin(admin.ModelAdmin):
    list_display = ("nome", "funcao",)

admin.site.register(Setor, SetorAdmin)