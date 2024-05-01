from django.db import models

# Create your models here
class user_info(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.email}'


class rating_by_user(models.Model):
    star = models.IntegerField()
    comment = models.CharField(max_length=255)