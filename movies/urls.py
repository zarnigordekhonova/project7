from django.urls import path
from movies.views import get_movie_info


urlpatterns = [
    path('movie', get_movie_info)
]