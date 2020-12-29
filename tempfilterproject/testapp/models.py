from django.db import models

# Create your models here.
class FilterClass(models.Model):
    name=models.CharField(max_length=40)
    addr=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    date=models.DateField()
