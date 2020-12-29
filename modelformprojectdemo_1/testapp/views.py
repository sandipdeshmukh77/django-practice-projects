from django.shortcuts import render
from .forms import StudentForm
from .models import  Student
# Create your views here.
def student_form_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request,'testapp/registration.html',{'form':form})
