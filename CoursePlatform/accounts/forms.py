from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from .models import Student, Profile
from functools import partial
from django.contrib.auth.models import User,Group

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class FullUserCreationForm(forms.Form):

    
    
    email = forms.EmailField(required=True)
    type = forms.ModelChoiceField(queryset=Group.objects.all())
    username=forms.CharField(
        required=True,
         strip=True,
        
        )
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
      
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        
    )
    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        email=cleaned_data.get('email')
        password1=cleaned_data.get('password1') 
        password2=cleaned_data.get('password2')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already registered')

       
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already registered')

        if password1 != password2:
            raise forms.ValidationError('Password Conformation Doesnt match')
        return cleaned_data 


    


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating common fields for all types of users: email, username
    """
    class Meta:
        model = Student
        fields = ["email"]


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating student's profile details
    """
    profile_pic = forms.ImageField(label='Profile picture', required=False,
                                   error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['profile_pic', 'first_name', 'last_name', 'gender', 'birth_date', 'country']