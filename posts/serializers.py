from rest_framework import serializers
from pathlib import Path
from taggit.serializers import TagListSerializerField, TaggitSerializer
from .models import Post
from likes.models import Like


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    """
    Serializer for the Post model, checks for owner of the post.
    Comment and download counts.
    Has tagging functionality, and image size validation.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
        )
    comments_count = serializers.SerializerMethodField()
    download_count = serializers.ReadOnlyField()
    tags = TagListSerializerField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        path = Path(value.name)
        file_extension = path.suffix.lower()
        valid_extensions = ['.jpg', '.jpeg', '.png']
        if file_extension not in valid_extensions:
            raise serializers.ValidationError(
                'Image must be jpg, jpeg or png!'
            )
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 5MB!'
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

    def get_like_id(self, obj):
        """
        Gets the like id if the user has liked the post.
        If user is not authenticated, or has not liked the post,
        return None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user,
                post=obj
            ).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj):
        """
        Returns the number of likes for the post.
        "likes" is referencing the Like model, connected to the Post model,
        through related_name="likes".
        """
        return obj.likes.count()

    def get_comments_count(self, obj):
        """
        Returns the number of comments for the post.
        "comments" is referencing the Comment model,
        connected to the Post model,
        through related_name="comments".
        """
        return obj.comments.count()

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
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
            'like_id',
            'likes_count',
        ]
