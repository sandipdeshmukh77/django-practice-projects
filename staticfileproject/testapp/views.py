from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')
def test(request):
    return render(request,'testapp/test.html')    
