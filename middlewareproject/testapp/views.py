from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request):
    print('this line added by view function')
    # print(10/0)
    return HttpResponse('<h1>this is demo text</h1>')
