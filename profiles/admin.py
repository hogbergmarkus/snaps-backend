from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Register Profile model in the admin panel
    """
    list_display = (
        'owner',
        'username',
        'created_at',
        'updated_at',
        'image',
    )
    list_filter = (
        'username',
        'owner',
    )
