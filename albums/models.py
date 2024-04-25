from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Album(models.Model):
    """
    Album model related to User and Post.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='albums',
        )
    title = models.CharField(max_length=255, blank=False, default='New Album')
    posts = models.ManyToManyField(Post, related_name='albums', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
