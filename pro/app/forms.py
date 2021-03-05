from django.core import validators
from django import forms
class doc (forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    mobile = forms.IntegerField(error_messages={'required':'Enter Your mobile'})
    city = forms.CharField(error_messages={'required':'Enter Your city'})
    email = forms.EmailField(error_messages={'required':'Enter Your email'})
    password = forms.CharField(min_length=6, max_length=8, widget=forms.PasswordInput,error_messages={'required':'Enter Your password'})

