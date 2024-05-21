from django.contrib import admin
from .models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """
    Register Album model in the admin panel
    """
    list_display = (
        'owner',
        'title',
        'updated_at',
    )
    list_filter = (
        'owner',
        'updated_at',
    )
