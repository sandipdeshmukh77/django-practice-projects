from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    rdate = models.IntegerField()
    rating = models.IntegerField()
