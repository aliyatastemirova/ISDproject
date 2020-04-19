from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    :param sender: User class (model used for authentication)
    :param instance: new user instance
    :param created: boolean (created a new user or not)
    :param kwargs:
    :return: nothing
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    :param sender: User class (model used for authentication)
    :param instance: new user instance
    :param kwargs:
    :return: nothing
    """
    instance.profile.save()
