from django.db import models

# Create your models here.
class parent1(models.Model):
    f1=models.CharField(max_length=150)
    f2=models.EmailField()
    f3=models.CharField(max_length=100)

class parent2(models.Model):
    f4=models.IntegerField()
    f5=models.IntegerField()
class child(parent1,parent2):
    f6=models.CharField(max_length=120)
    f7=models.IntegerField()
