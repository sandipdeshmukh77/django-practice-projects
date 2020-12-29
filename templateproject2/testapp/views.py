from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    date=datetime.datetime.now()
    name='sandip'
    position='data scientist'
    age=29
    my_dict={'date':date,'name':name,'position':position,'age':age}
    return render(request,'testapp/testapp.html',context=my_dict)
