from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish2(response):
    return HttpResponse('<h1>this text is from secondapp</h1>')


    
