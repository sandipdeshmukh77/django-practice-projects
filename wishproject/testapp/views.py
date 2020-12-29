from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    dt=datetime.datetime.now()
    date=int(dt.strftime("%H"))
    msg='hello Guest!!! very  '
    if (date<12):
        msg+='good morning!!!'
    elif (date<16):
        msg+='good afternoon!!!'
    elif (date<21):
        msg+='good evening!!!'
    else:
        msg+='good Night!!!'
    my_dict={'insert_date':dt,'insert_msg':msg}
    return render(request,'testapp/index.html',context=my_dict)
