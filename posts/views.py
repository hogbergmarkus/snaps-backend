from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from snaps_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    Returns a list of all posts.
    A post can be created by an authenticated user.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter
    ]
    search_fields = [
        'owner__username',
        'title',
        'tags__name',
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
