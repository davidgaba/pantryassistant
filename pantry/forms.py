from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import PantryItem


class CreateUserForm(UserCreationForm):
    '''
        Create or register a user (Model Form)
    '''
    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    first_name = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input', 'placeholder':'First Name'}), label='First Name')
    last_name = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input', 'placeholder':'Last Name'}), label='Last Name')
    username = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input', 'placeholder':'Userame'}), label='Username')
    email = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input', 'placeholder':'Email'}), label='Email')


class LoginForm(AuthenticationForm):
    '''
        Authenticate a user (Model Form)
    '''
    username = forms.CharField(required=True, widget=TextInput(attrs={'placeholder':'Username'}), label='')
    password = forms.CharField(required=True, widget=PasswordInput(attrs={'placeholder':'Password'}), label='')


class NewPantryItemForm(forms.ModelForm):
    '''
        Add a pantry item (Model Form)
    '''
    class Meta:
        model = PantryItem
        fields = ['name', 'quantity', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].required = False
        self.fields['expiration_date'].required = False
        self.fields['expiration_date'].label = "Expiration Date (Optional)"

    name = forms.CharField(required=True, widget=forms.TextInput(), label='Item Name')
    quantity = forms.IntegerField(required=False, widget=forms.TextInput(), label='Quantity (Optional)')
