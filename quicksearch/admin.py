from django.contrib import admin

from .models import Actor
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name', 'normalized_name']})
            ]
    list_display = ('name', 'normalized_name')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ("name", 'normalized_name')
