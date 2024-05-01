from django.db import models

# Create your models here.
class Movie_info(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    based_on_book = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.title} {self.year}'

class Movie_rating(models.Model):
    number_awards = models.IntegerField()
    rate_percentage_on_ImDB = models.IntegerField()

    def __str__(self):
        return f'{self.rate_percentage_on_ImDB} {self.number_awards}'