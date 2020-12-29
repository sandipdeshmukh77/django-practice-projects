from django.shortcuts import render
from . import forms
# Create your views here.
def feedbackform_view(request):
    form=forms.feedbackform()

    if request.method=='POST':
        form=forms.feedbackform(request.POST)
    if form.is_valid():
        print('name:',form.cleaned_data['name'])
        print('rollno:',form.cleaned_data['rollno'])
        print('email:',form.cleaned_data['email'])
        print('phonenumber:',form.cleaned_data['phonenumber'])
        print('feedback:',form.cleaned_data['feedback'])
    return render(request,'testapp/fb.html',{'form':form})
