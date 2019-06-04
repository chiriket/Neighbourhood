from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Neighbourhood, Business,Profile,Post

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin,occupants']


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = []

class ProfileForm(forms.ModelForm):   
    class Meta:
        model = Profile
        exclude = ['user']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','neighborHood','pub_date']



