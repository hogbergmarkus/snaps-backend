from django.contrib.auth.models import User
from .models import Comment
from posts.models import Post
from rest_framework.test import APITestCase
from rest_framework import status


class CommentListViewTests(APITestCase):
    """
    Tests for the Comment list view.
    List comments, create a comment, logged out user cannot create a comment.
    """
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(owner=brian, title='this is a title')

    def test_can_list_comments(self):
        adam = User.objects.get(username='adam')
        post = Post.objects.get(title='this is a title')
        Comment.objects.create(
            owner=adam, post=post, content='this is a comment'
            )
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='adam', password='pass')
        post = Post.objects.get(title='this is a title')
        response = self.client.post(
            '/comments/', {'post': post.id, 'content': 'this is a comment'}
            )
        count = Comment.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cannot_create_comment(self):
        post = Post.objects.get(title='this is a title')
        response = self.client.post(
            '/comments/', {'post': post.id, 'content': 'this is a comment'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CommentDetailViewTests(APITestCase):
    """
    Tests for the Comment detail view.
    Get single comment, update a comment, delete a comment.
    Logged out user cannot update or delete a comment.
    """
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Post.objects.create(owner=brian, title='this is a title')

    def test_can_retrieve_a_single_comment(self):
        adam = User.objects.get(username='adam')
        post = Post.objects.get(title='this is a title')
        comment = Comment.objects.create(
            owner=adam, post=post, content='this is a comment'
            )
        response = self.client.get(f'/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_update_comment(self):
        self.client.login(username='adam', password='pass')
        post = Post.objects.get(title='this is a title')
        comment = Comment.objects.create(
            owner=User.objects.get(username='adam'),
            post=post,
            content='this is a comment'
            )
        response = self.client.put(
            f'/comments/{comment.id}/', {'content': 'new comment'}
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        comment.refresh_from_db()
        self.assertEqual(comment.content, 'new comment')

    def test_logged_out_user_cannot_update_comment(self):
        post = Post.objects.get(title='this is a title')
        comment = Comment.objects.create(
            owner=User.objects.get(username='adam'),
            post=post,
            content='this is a comment'
            )
        response = self.client.put(
            f'/comments/{comment.id}/', {'content': 'new comment'}
            )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_delete_comment(self):
        self.client.login(username='adam', password='pass')
        post = Post.objects.get(title='this is a title')
        comment = Comment.objects.create(
            owner=User.objects.get(username='adam'),
            post=post,
            content='this is a comment'
            )
        response = self.client.delete(f'/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logged_out_user_cannot_delete_comment(self):
        post = Post.objects.get(title='this is a title')
        comment = Comment.objects.create(
            owner=User.objects.get(username='adam'),
            post=post,
            content='this is a comment'
            )
        response = self.client.delete(f'/comments/{comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
