from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    '''
        Create or register a user (Model Form)
    '''
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.CharField(required=True)

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    '''
        Authenticate a user (Model Form)
    '''
    username = forms.CharField(required=True, widget=TextInput())
    password = forms.CharField(required=True, widget=PasswordInput())