from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile.save()
        
@receiver(post_delete, sender=User)
def delete_user_profile(sender, instance, **kwargs):
    # Delete the associated Profile when a User is deleted
    if hasattr(instance, 'profile'):
        instance.profile.delete()