from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from .models import Student
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
