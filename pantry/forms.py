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

    first_name = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input'}), label='First Name')
    last_name = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input'}), label='Last Name')
    username = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input'}), label='Username')
    email = forms.CharField(required=True, widget=TextInput(attrs={'class':'form-input'}), label='Email')


class LoginForm(AuthenticationForm):
    '''
        Authenticate a user (Model Form)
    '''
    username = forms.CharField(required=True, widget=TextInput(attrs={'class':'login-input', 'placeholder':'Username'}), label='')
    password = forms.CharField(required=True, widget=PasswordInput(attrs={'class':'login-input', 'placeholder':'Password'}), label='')


class NewPantryItemForm(forms.ModelForm):
    '''
        Add a pantry item (Model Form)
    '''
    class Meta:
        model = PantryItem
        fields = ['name', 'quantity', 'units', 'expiration_date']
        widgets = {
            'quantity' : forms.NumberInput(attrs={'min': 0}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].required = False
        self.fields['quantity'].label = "Quantity (Optional)"
        self.fields['units'].required = False
        self.fields['units'].label = "Units (Optional)"
        self.fields['expiration_date'].required = False
        self.fields['expiration_date'].label = "Expiration Date (Optional)"

    name = forms.CharField(required=True, widget=forms.TextInput(), label='Item Name')


class EditPantryItemForm(forms.ModelForm):
    '''
        Edit an item's fields (Model Form)
    '''
    class Meta:
        model = PantryItem
        fields = ['quantity', 'expiration_date']
        widgets = {
            'quantity' : forms.NumberInput(attrs={'min': 0}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].required = False
        self.fields['quantity'].label = "Quantity"
        self.fields['expiration_date'].required = False
        self.fields['expiration_date'].label = "Best Before Date"

    