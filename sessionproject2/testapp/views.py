from django.shortcuts import render
from testapp.forms import NameForm,AgeForm,CityForm

# Create your views here.
def name_view(request):
    form=NameForm()
    return render(request,'testapp/name.html',{'form':form})

def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=AgeForm()
    return render(request,'testapp/age.html',{'form':form})

def city_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=CityForm()
    return render(request,'testapp/city.html',{'form':form})

def result_view(request):
    city=request.GET['city']
    request.session['city']=city
    return render(request,'testapp/result.html')
