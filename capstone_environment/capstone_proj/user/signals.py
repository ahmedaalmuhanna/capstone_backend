
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, User
from django.contrib.auth import get_user_model


User = get_user_model()

@receiver(post_save, sender = User)
def create_or_save_user_profile(sender, created, instance, **kwargs):
    if created == True:
        Profile.objects.create(user = instance)
    instance.profile.save()