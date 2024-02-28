from django import forms 
from .models import Musician,Album
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register_form(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_date' : forms.DateInput(attrs={'type':'date'})
        }
