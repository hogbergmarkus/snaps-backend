from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Register Like model in the admin panel
    """
    list_display = (
        'owner',
        'post',
        'comment',
        'created_at',
    )
    list_filter = (
        'owner',
        'post',
        'comment',
    )
