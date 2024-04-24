from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    Includes logic to prevent duplicate likes.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Creates a Like instance.
        Checks if the user already liked the post.
        Throws an error if the user already liked the post.
        """
        owner = self.context['request'].user
        post = validated_data.get('post')
        comment = validated_data.get('comment')

        if Like.objects.filter(
            owner=owner,
            post=post,
            comment=comment
        ).exists():
            raise serializers.ValidationError('You already liked this')

        return super().create(validated_data)

    class Meta:
        model = Like
        fields = [
            'id',
            'owner',
            'post',
            'comment',
            'created_at',
        ]
