from django import forms

class StudentApplication(forms.Form):
    Name=forms.CharField()
    Marks=forms.IntegerField()
