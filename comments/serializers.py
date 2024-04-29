from rest_framework import serializers
from .models import Comment
from likes.models import Like


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
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Gets the like id if the user has liked the comment.
        If user is not authenticated, or has not liked the comment,
        return None.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user,
                comment=obj
            ).first()
            return like.id if like else None
        return None

    def get_likes_count(self, obj):
        """
        Returns the number of likes for the comment.
        "likes" is referencing the Like model, connected to the Comment model,
        through related_name="likes".
        """
        return obj.likes.count()

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
            'like_id',
            'likes_count',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Makes sure that the comment is associated with the correct post
    when being edited.
    """
    post = serializers.ReadOnlyField(source='post.id')
