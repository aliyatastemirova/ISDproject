from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from .models import Student, Profile
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class FullUserCreationForm(UserCreationForm):
    """
    Extends standard usercreationform by including email address
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = Student
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    """
    A form for updating common fields for all types of users: email, username
    """
    class Meta:
        model = Student
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    """
    A form for updating student's profile details
    """
    profile_pic = forms.ImageField(label='Profile picture', required=False,
                                   error_messages={'invalid': "Image files only"}, widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['profile_pic', 'first_name', 'last_name', 'gender', 'birth_date', 'country']