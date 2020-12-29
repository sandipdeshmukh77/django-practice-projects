from django import forms

class feedbackform(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    phonenumber=forms.IntegerField()
    feedback=forms.CharField(widget=forms.Textarea)
