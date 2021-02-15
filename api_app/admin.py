from django.contrib import admin

# Register your models here.
from .models import Pokemon


class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Pokemon, PokemonAdmin)
