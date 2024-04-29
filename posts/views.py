from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from snaps_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    Returns a list of all posts.
    A post can be created by an authenticated user.
    In the queryset, annotate the number of likes for each post,
    related to Post through related_name="likes".
    """
    queryset = Post.objects.annotate(
        likes_count=Count('likes'),
        comments_count=Count('comments'),
    )
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'tags__name',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides the details for a single post,
    update and delete it if you own it.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
