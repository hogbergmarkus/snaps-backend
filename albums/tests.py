from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Album


class AlbumListViewTests(APITestCase):
    """
    Tests for the Album list view.
    Users can create albums and list albums.
    Unauthenticated users cannot create or list albums.
    Users can only list their own albums.
    """

    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(
            username='brian', password='pass'
            )

    def test_logged_in_user_can_create_album(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/albums/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_album(self):
        response = self.client.post('/albums/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_list_albums(self):
        self.client.login(username='adam', password='pass')
        Album.objects.create(owner=self.adam, title='My Album')
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cannot_list_albums(self):
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_cannot_list_other_users_albums(self):
        self.client.login(username='adam', password='pass')
        Album.objects.create(owner=self.brian, title='My Album')
        response = self.client.get('/albums/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
