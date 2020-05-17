from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group


# Create your models here.
class User(AbstractUser):
    """
    Right now only users can be only students, added to Students group upon registration.
    User class uses AbstractUser for flexibility in future
    """
    email = models.EmailField(max_length=100, null=False, unique=True)
    is_student = models.BooleanField(null=False, default=False)
    is_partner = models.BooleanField(null=False, default=False)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Profile(models.Model):
    """
    Profile is created automatically when a user is created
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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True,default="M")
    birth_date = models.DateField(max_length=30, null=True)
    country = CountryField(max_length=50, null=True)
    email_confirmed = models.BooleanField(default=False)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f'{self.user.username} Profile'


students, created = Group.objects.get_or_create(name='Students')
partners, created = Group.objects.get_or_create(name='Partners')
