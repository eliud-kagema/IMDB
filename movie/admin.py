from django.contrib import admin

from . models import Movie, MovieLinks, Person, Role



admin.site.register(MovieLinks)


admin.site.register(Person)

admin.site.register(Role)



@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'language', 'status', 'director']
    # fields = [('title'), ('image', 'category'), ('language', 'status'),  ('director', 'year_of_prodcution'), ('writers'), ('rating', 'views_count'), ('description')]
    list_filter = ['category', 'language', 'director']
    list_editable = ['status']



     
    

