from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
import pytest
from django.contrib.auth.models import User, Group

@pytest.fixture(scope="module")
def create_group():
    group = Group.objects.create(name='limite')
    return group

class PublicPostsTests(APITestCase):
    @pytest.mark.django_db
    def test_get_posts_anonymous_fails(self, create_group):
        group = create_group()
        user = User.objects.create_user(
            username='test',
            email='test@test.com',
            password='password2023',
            groups=[group]
        )

        self.client.force_authenticate(user)

        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 401)


class PrivatePostsTests(APITestCase):
    def setUp(self, create_group):
        self.user = User.objects.create_user(
            username='test2',
            email='test2@test.com',
            password='testpass2023',
            groups=[create_group()]
        )

        self.client.force_authenticate(self.user)

    def test_get_posts_authenticated_works(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)