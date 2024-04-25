from rest_framework import generics, permissions
from .models import Album
from .serializers import AlbumSerializer


class AlbumList(generics.ListCreateAPIView):
    """
    Returns a list of all albums.
    An album can be created by an authenticated user.
    Only the owner can list their albums.
    """
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View a single album if you own it.
    Update or delete it if you own it.
    """
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(owner=user)
