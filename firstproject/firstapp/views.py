from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s='<h1> this is the test note for django project</h1>'
    return HttpResponse(s)
