from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the comment model.
    is_owner, profile_id and profile_image are added
    when returning a list of Comment instances.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'post',
            'content',
            'is_owner',
            'profile_id',
            'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Makes sure that the comment is associated with the correct post
    when being edited.
    """
    post = serializers.ReadOnlyField(source='post.id')
