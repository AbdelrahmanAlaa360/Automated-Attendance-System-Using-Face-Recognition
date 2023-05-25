from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import  User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class ProfileImageForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))


class TrainingImageForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file', 'multiple': True}), required=False)