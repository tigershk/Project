from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    imdbid = models.CharField(max_length=50)

    def __str__(self):
        return self.title