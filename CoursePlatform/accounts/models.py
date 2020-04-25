from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Student(AbstractUser):
    """
    Right now only users can be only students.
    Student class uses AbstractUser for flexibility in future
    """
    email = models.EmailField(max_length=100, null=False, unique=True)

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.username


class Profile(models.Model):
    """
    Profile is created automatically when a Student user is created
    It's necessary to collect more information than what is gathered during registration
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    birth_date = models.DateField(max_length=30, null=True)
    country = CountryField(max_length=50, null=True)
    email_confirmed = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f'{self.user.username} Profile'


