from django import forms
from newapp.models import wallet
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    id = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField()
    money = forms.CharField()
    class Meta():
        model = User
        fields = ('id','name','money')
