from django.contrib import admin

from . models import Movie, MovieLinks



admin.site.register(MovieLinks)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'language', 'status', 'director']
    list_filter = ['category', 'language', 'director']
    list_editable = ['status']
