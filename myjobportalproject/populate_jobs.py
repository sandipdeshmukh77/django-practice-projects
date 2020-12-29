import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myjobportalproject.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
	num=str(randint(6,9))
	for i in range(9):
		num=num+str(randint(0,9))
	return int(num)
def populate(n):
    for i in range(n):
         fdate=fake.date()
         fcompany=fake.company()
         ftitle=fake.random_element(elements=('software engineer','project lead','software developer','data scientist'))
         feligibility=fake.random_element(elements=('BE','M.tech','MCA','BCA','B.tech'))
         faddress=fake.address()
         femail=fake.email()
         fphonenumber=phonenumbergen()

         punejobs_record=punejobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
         hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
         chennaijobs_record=chennaijobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

populate(25)
