from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    profile_owner = serializers.ReadOnlyField(source='profile_owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.profile_owner

    class Meta:
        model = Profile
        fields = [
            'id',
            'profile_owner',
            'created_at',
            'updated_at',
            'username',
            'bio',
            'image',
            'is_owner',
        ]
