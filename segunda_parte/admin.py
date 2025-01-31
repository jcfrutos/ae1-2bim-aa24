from django.contrib import admin
from .models import Categoria, PlatoTipico

# Register your models here.
class PlatoTipicoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id','nombre','stock','creado_en','categoria')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')

admin.site.register(PlatoTipico, PlatoTipicoAdmin)
admin.site.register(Categoria,CategoriaAdmin)