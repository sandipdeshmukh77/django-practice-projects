from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(response):
    return HttpResponse("<h1>this is responce from first view</h1>")
def second_view(response):
    return HttpResponse("<h1>this is responce from second view</h1>")
def third_view(response):
    return HttpResponse("<h1>this is responce from third view</h1>")
def fourth_view(response):
    return HttpResponse("<h1>this is responce from fourth view</h1>")
