from django import forms

class AddItems(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()
