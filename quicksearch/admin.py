from django.contrib import admin

from .models import Actor
from .models import Movie


# class CastInlineAdmin(admin.TabularInline):
#     verbose_name = 'Actor'
#     verbose_name_plural = 'Actors'
#     model = Movie.cast.through


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['name']})
    ]
    list_display = ('name',)
    # inlines = (CastInlineAdmin,)

#
# class FilmographyInlineAdmin(admin.TabularInline):
#     verbose_name = 'Movie'
#     verbose_name_plural = 'Movies'
#     model = Actor.filmography.through


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ("name",)
    # inlines = (FilmographyInlineAdmin,)
