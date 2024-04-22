from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """
    Serializer for the Post model, checks for owner of the post.
    Comment and download counts.
    Has tagging functionality, and image size validation.
    """

    post_owner = serializers.ReadOnlyField(source='post_owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='post_owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='post_owner.profile.image.url'
        )
    comments_count = serializers.ReadOnlyField()
    download_count = serializers.ReadOnlyField()
    tags = TagListSerializerField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.post_owner

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    class Meta:
        model = Post
        fields = [
            'id',
            'post_owner',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'tags',
            'download_count',
            'is_owner',
            'profile_id',
            'profile_image',
            'comments_count',
        ]
