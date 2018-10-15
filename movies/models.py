from django.db import models

class Movie(models.Model):
    movieid = models.CharField(max_length=50,default="")
    title = models.CharField(max_length=200)
    imdbid = models.CharField(max_length=50)
    overview = models.TextField(default="")

    def __str__(self):
        return self.title