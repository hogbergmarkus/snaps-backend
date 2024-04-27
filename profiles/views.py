from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.http import Http404
from .models import Profile
from .serializers import ProfileSerializer
from snaps_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    Returns a list of all profiles.
    Creation of profiles is handled by django signals,
    so every time a user signs up, a profile is created.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(APIView):
    """
    Returns a single profile.
    Get profile or return 404 if not found.
    The put method allows you to update a profile.
    IsOwnerOrReadOnly allows only the object owner to edit it.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            self.check_object_permissions(self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, context={'request': request}
            )
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(
            profile, data=request.data, context={'request': request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
