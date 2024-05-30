from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Automatically created profile for each user, that stores
    extra information about the user.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_d1hmel',
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance, username=instance.username)


def update_user_username(sender, instance, **kwargs):
    user = instance.owner
    if user.username != instance.username:
        user.username = instance.username
        user.save()


post_save.connect(create_profile, sender=User)
post_save.connect(update_user_username, sender=Profile)
