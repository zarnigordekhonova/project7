from django.contrib import admin
from users.models import user_info, rating_by_user

# Register your models here.

admin.site.register(user_info)
admin.site.register(rating_by_user)
