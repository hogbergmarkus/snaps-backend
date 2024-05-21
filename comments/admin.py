from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Register Comment model in the admin panel
    """
    list_display = (
        'owner',
        'post',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'owner',
        'post',
        'updated_at',
    )
