from django.urls import path
from users.views import get_info_user


urlpatterns = [
    path('user', get_info_user)
]