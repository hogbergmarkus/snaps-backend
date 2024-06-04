from rest_framework import serializers
from .models import Report


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer for the Report model.
    """

    class Meta:
        model = Report
        fields = [
            'id',
            'post',
            'user',
            'reason',
            'reported_at',
        ]
