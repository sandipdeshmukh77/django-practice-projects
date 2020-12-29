from django.shortcuts import render
from . import forms
# Create your views here.
def feedbackview(request):
    form=forms.FeedbackForm()
    if request.method=='POST':
        form=forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('form validation success printing imformation')
            print('Name:',form.cleaned_data['name'])
            print('Roll NO:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
    
    return render(request,'testapp/register.html',{'form':form})
