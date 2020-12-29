from django.shortcuts import render
from testapp.models import *
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')
def punejobs1(request):
    jobs_list=punejobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)
def hydjobs1(request):
    jobs_list=hydjobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)
def chennaijobs1(request):
    jobs_list=chennaijobs.objects.all()
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)
