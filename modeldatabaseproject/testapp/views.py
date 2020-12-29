from django.shortcuts import render
from testapp.models import Employee
# Create your views here.
emp_list=Employee.objects.all()
my_dict={'emp_list':emp_list}
def emp_info(request):
    return render(request,'testapp/emp.html',context=my_dict)
def index(request):
    return render(request,'testapp/index.html')
