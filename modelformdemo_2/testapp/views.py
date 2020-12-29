from django.shortcuts import render
from .forms import StudentForm
from . import models
# Create your views here.
def Student_view(request):
    form=StudentForm()
    if request.method == "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('data saved to db ')
    return render(request,'testapp/submit.html',{'form':form})
