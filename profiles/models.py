from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Automatically created profile for each user, that stores
    extra information about the user.
    """
    profile_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_d1hmel',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.profile_owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(profile_owner=instance)


post_save.connect(create_profile, sender=User)
