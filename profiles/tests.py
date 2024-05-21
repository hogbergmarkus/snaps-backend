from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Profile
from rest_framework import status


class ProfileListViewTests(APITestCase):
    """
    Tests for the Profile list view.
    Profiles can be listed.
    """
    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    """
    Tests for the Profile detail view.
    Profiles can be retrieved.
    Profiles can only be updated by their owner.
    """
    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.adam_profile = Profile.objects.get(owner=self.adam)
        self.brian = User.objects.create_user(
            username='brian', password='pass'
            )

    def test_can_retrieve_profile(self):
        response = self.client.get(f'/profiles/{self.adam_profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_can_update_profile(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put(
            f'/profiles/{self.adam_profile.id}/',
            {'username': 'mada'}
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.adam.refresh_from_db()
        self.assertEqual(self.adam.profile.username, 'mada')

    def test_logged_out_user_cannot_update_profile(self):
        response = self.client.put(
            f'/profiles/{self.adam_profile.id}/',
            {'username': 'mada'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_cannot_update_other_users_profile(self):
        self.client.login(username='brian', password='pass')
        response = self.client.put(
            f'/profiles/{self.adam_profile.id}/',
            {'username': 'mada'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_owner_can_delete_profile(self):
        self.client.login(username='adam', password='pass')
        response = self.client.delete(f'/profiles/{self.adam_profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(f'/profiles/{self.adam_profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_out_user_cannot_delete_profile(self):
        response = self.client.delete(f'/profiles/{self.adam_profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_cannot_delete_other_users_profile(self):
        self.client.login(username='brian', password='pass')
        response = self.client.delete(f'/profiles/{self.adam_profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.get(f'/profiles/{self.adam_profile.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
