from django import forms
from django.core import validators
def starts_with_d(value):
    if value.isalpha() != True:
        raise forms.ValidationError('alphabatical')

class feedbackform(forms.Form):
    name=forms.CharField(validators=[starts_with_d])
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)
    phonenumber=forms.IntegerField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(30),validators.MinLengthValidator(10)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    def clean(self):
        cleaned_data=super().clean()
        inputpwd=cleaned_data['password']
        inputrpwd=cleaned_data['rpassword']
        if inputpwd != inputrpwd:
            raise forms.ValidationError('password not matched')
        input_bot_handler= cleaned_data['bot_handler']
        if len(input_bot_handler)>0:
            raise forms.ValidationError('thank you BOT')   
    #     inputname=self.cleaned_data['name']
    #     if len(inputname) < 4:
    #         raise forms.ValidationError('the lenght of name should be greater than four')
    #     inputrollno=self.cleaned_data['rollno']
    #     if (inputrollno)>100:
    #         raise forms.ValidationError('the rollno should less than 100')
    #     inputemail=self.cleaned_data['email']
    #     print('validating email successful')
    #     inputfeedback=self.cleaned_data['feedback']
    #     print('validating feedback successful')
