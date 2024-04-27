from django.contrib.auth.models import User
from rest_framework.test import APITestCase
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
