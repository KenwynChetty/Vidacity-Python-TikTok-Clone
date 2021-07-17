from accounts.models import Profile
from django.contrib.auth.models import User
from django import forms


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta: 
        model =  User
        fields = ['username','first_name','last_name','email']


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Enter Your Bio'}))
    relationship = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Example: Single'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'type':'number','placeholder':'Enter Your Age'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Enter Your Location'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'type':'file','id':'document-upload', 'onchange':'upload()'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'type':'number','placeholder':'Example: 27662203972 '}))

    class Meta:
        model = Profile
        fields = ['image','birth_date','age','relationship','location','bio','contact']