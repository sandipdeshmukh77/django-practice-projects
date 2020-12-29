from django.db import models
from django.db.models.functions import Lower
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by(Lower('eno'))

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gt=18000)

class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lt=13000)



# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    eaddr=models.CharField(max_length=100)
    esal=models.FloatField()
    objects=CustomManager()

class ProxyEmployee2(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployee3(Employee):
    objects=CustomManager3()
    class Meta:
        proxy=True
