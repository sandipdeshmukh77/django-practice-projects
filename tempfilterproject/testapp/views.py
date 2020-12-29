from django.shortcuts import render
from testapp.models import FilterClass
# Create your views here.

def UpperView(request):
    data_list=FilterClass.objects.all()
    return render(request,'testapp/upper.html',{'data_list':data_list})
def LowerView(request):
    data_list=FilterClass.objects.all()
    return render(request,'testapp/lower.html',{'data_list':data_list})
