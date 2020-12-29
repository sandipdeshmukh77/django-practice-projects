from django.shortcuts import render
from testapp import forms
# Create your views here.
def student_view(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('form data inserted successfully')
    return render(request,'testapp/mform.html',{'form':form})
