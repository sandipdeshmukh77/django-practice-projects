from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
# Create your views here.
def emp_view(request):
    employee=Employee.objects.all()
    return render(request,'testapp/index.html',{'employee':employee})

def emp_form_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    return render(request,'testapp/form.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'testapp/update.html',{'employee':employee})
