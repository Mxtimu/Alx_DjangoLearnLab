from django.db.models.signals import post_save
from django.conf import settings # <-- FIX 1
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL) # <-- FIX 2
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='Member')

@receiver(post_save, sender=settings.AUTH_USER_MODEL) # <-- FIX 3
def save_user_profile(sender, instance, **kwargs):
    # We check if the user profile exists before saving
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()