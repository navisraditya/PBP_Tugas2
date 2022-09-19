from django.db import models

# Create your models here.
class watchlist(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()