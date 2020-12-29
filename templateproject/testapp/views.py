from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    my_dict={'date_msg':date}
    return render(request, 'testapp/testapp.html',context=my_dict)
