from django.shortcuts import render
from . import form

# Create your views here.
def StudentApplicationform(request):
    san=form.StudentApplication()
    return render(request,'testapp/register.html',{'form':san})
