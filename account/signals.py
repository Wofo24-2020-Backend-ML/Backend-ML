from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import Professional

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Professional.objects.create(user=instance)
        print("Profile Created")

@receiver(post_save, sender=User)
def update_profile(sender, instance, **kwargs):
    instance.professional.save()