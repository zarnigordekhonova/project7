from django.contrib import admin
from movies.models import Movie_info, Movie_rating

# Register your models here.

admin.site.register(Movie_info)
admin.site.register(Movie_rating)

