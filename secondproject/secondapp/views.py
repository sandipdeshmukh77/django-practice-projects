from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def pune(response):
    s='<h1>this is jobs openings in pune</h1>'
    return HttpResponse(s)
def mumbai(response):
    s='<h1>this is jobs openings in mumbai</h1>'
    return HttpResponse(s)
def hyderabad(response):
    s='<h1>this is jobs openings in hyderabad</h1>'
    return HttpResponse(s)
def chennai(response):
    s='<h1>this is jobs openings in chennai</h1>'
    return HttpResponse(s)
def datetime(response):
    time=datetime.datetime.now()
    s='<h1>this is current time of server :'+str(time)+'</h1>'
    return HttpResponse(s)
