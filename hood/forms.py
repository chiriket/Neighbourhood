from django import forms
from .models import Profile, Reviews
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Neighbourhood, Business

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['name', 'occupants', 'location', ]


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['user']


    
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighbourhood']

