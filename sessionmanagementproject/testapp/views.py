from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'testapp/name.html')

def city_view(request):
    name=request.GET['name']
    response=render(request,'testapp/city.html')
    response.set_cookie('name',name)
    return response

def education_view(request):
    city=request.GET['city']
    response=render(request,'testapp/education.html')
    response.set_cookie('city',city)
    return response
def result_view(request):
    education=request.GET['education']
    name=request.COOKIES.get('name')
    city=request.COOKIES.get('city')
    response=render(request,'testapp/result.html',{'education':education,'name':name,'city':city})
    return response
