from django import forms
from django.contrib.auth.models import User
from bank.models import UserProfileInfo

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('img','dob','phone','blood_group')
