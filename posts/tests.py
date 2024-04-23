from django.contrib.auth.models import User
from .models import Post
from rest_framework.test import APITestCase
from rest_framework import status


class PostListViewTests(APITestCase):
    """
    Tests for the Post list view.
    List posts, create a post, logged out user cannot create a post.
    """
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_posts(self):
        adam = User.objects.get(username='adam')
        Post.objects.create(owner=adam, title='this is a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post(
            '/posts/', {'title': 'this is a title', 'tags': 'tag1, tag2'}
            )
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_post(self):
        response = self.client.post(
            '/posts/', {'title': 'this is a title', 'tags': 'tag1, tag2'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    """
    Tests for the Post detail view.
    Get single post, update a post, delete a post.
    Logged out user cannot update or delete a post.
    """
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_retrieve_a_single_post(self):
        adam = User.objects.get(username='adam')
        post = Post.objects.create(owner=adam, title='this is a title')
        response = self.client.get(f'/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_update_post(self):
        self.client.login(username='adam', password='pass')
        post = Post.objects.create(
            owner=User.objects.get(username='adam'), title='this is a title'
            )
        response = self.client.put(
            f'/posts/{post.id}/', {'title': 'new title', 'tags': 'tag1, tag2'}
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, 'new title')

    def test_logged_out_user_cannot_update_post(self):
        post = Post.objects.create(
            owner=User.objects.get(username='adam'), title='this is a title'
            )
        response = self.client.put(
            f'/posts/{post.id}/', {'title': 'new title', 'tags': 'tag1, tag2'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_delete_post(self):
        self.client.login(username='adam', password='pass')
        post = Post.objects.create(
            owner=User.objects.get(username='adam'), title='this is a title'
            )
        response = self.client.delete(f'/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logged_out_user_cannot_delete_post(self):
        post = Post.objects.create(
            owner=User.objects.get(username='adam'), title='this is a title'
            )
        response = self.client.delete(f'/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
