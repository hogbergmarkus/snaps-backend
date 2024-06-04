from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from posts.models import Post


class ReportListViewTests(APITestCase):
    """
    Tests for the Report list view.
    Users can create reports.
    Unauthenticated users cannot create reports.
    """

    def setUp(self):
        self.adam = User.objects.create_user(username='adam', password='pass')
        self.brian = User.objects.create_user(
            username='brian', password='pass'
            )
        self.post = Post.objects.create(
            title='Test Post', content='Test Content', owner=self.adam
            )

    def test_logged_in_user_can_create_report(self):
        self.client.login(username='adam', password='pass')
        data = {
            'post': self.post.id,
            'user': self.adam.id,
            'reason': 'Inappropriate content',
        }
        response = self.client.post('/reports/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_report(self):
        data = {
            'post': self.post.id,
            'user': self.adam.id,
            'reason': 'Inappropriate content',
        }
        response = self.client.post('/reports/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cannot_create_report_without_reason(self):
        self.client.login(username='adam', password='pass')
        data = {
            'post': self.post.id,
            'user': self.adam.id,
            'reason': '',
        }
        response = self.client.post('/reports/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
