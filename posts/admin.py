from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Register Post model in the admin panel
    """
    list_display = (
        'owner',
        'title',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'owner',
    )
