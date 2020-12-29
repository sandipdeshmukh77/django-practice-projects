import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ormproject1.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()

def populate(n):
    for i in range(n):
         feno=randint(1000,9999)
         fename=fake.name()
         feaddr=fake.city()
         fesal=randint(10000,20000)

         emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,eaddr=feaddr,esal=fesal)

populate(30)
