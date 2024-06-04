from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """
    Register Report model in the admin panel
    """
    list_display = (
        'user',
        'post',
        'reported_at',
    )
    list_filter = (
        'user',
        'post',
    )
