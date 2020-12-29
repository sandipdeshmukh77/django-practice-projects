from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models import Avg,Sum,Min,Max,Count
from django.db.models.functions import Lower
# Create your views here.
def emp_view(request):
    employee=Employee.objects.get_emp_sal_range(15000,20000)
    #employee=Employee.objects.filter(~Q(esal__gt=18000))
    return render(request,'testapp/display.html',{'employee':employee})
