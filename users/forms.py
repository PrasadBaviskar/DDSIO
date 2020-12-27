from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password']

        widgets = {
            "first_name": forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'required': 'required'}),
            "last_name": forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'required': 'required'}),
            "username": forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'required': 'required'}),
            "password": forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control', 'required': 'required'})
        }

# for addition field - contact
class UserForm_1(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['contact']
        widgets = {
            "contact": forms.TextInput(
                attrs={'placeholder': 'Mobile No', 'class': 'form-control', 'required': 'required'}),
            }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields="__all__"
        fields = ['position','birthdate','gender']
        widgets = {
            'position': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
            'birthdate': forms.DateInput(attrs={'placeholder': 'Eg. 2020-07-01', 'class': 'form-control', 'data-toggle': 'flatpickr', 'required': 'required'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        }
