from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1> hello guest very'
    if h<12:
        msg=msg+'good morning'
    elif h<4:
        msg=msg+'good afternoon'
    elif h<9:
        msg=msg+'good evening'
    else:
        msg=msg+'good night'
    msg=msg+'</h1><hr>'
    msg=msg+'<h1>now server time is '+str(date)+'</h1>'
    return HttpResponse(msg)
