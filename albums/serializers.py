from rest_framework import serializers
from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for the Album model.
    Extra fields for the owner, profile_id and is_owner.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Album
        fields = [
            'id',
            'owner',
            'title',
            'posts',
            'created_at',
            'updated_at',
        ]
