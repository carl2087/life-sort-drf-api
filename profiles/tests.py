from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class TestRootRouteView(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        carltest = User.objects.get(username='carltest')

    def test_logged_out_user_can_access_root_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_access_root_route(self):
        self.client.login()
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProfileListView(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        carltest = User.objects.get(username='carltest')

    def test_logged_out_user_can_access_profile_list(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_access_profile_list(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestProfileListDetailView(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        User.objects.create_user(username='junotest', password='testjuno')

    def test_logged_out_user_access_profile_detail_view(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_access_profile_detail_view(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_access_other_users_profile(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_edit_their_own_profile(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put('/profiles/1/', {
            'name': 'a new name'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_edit_another_user_profile(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put('/profiles/2/', {
            'name': 'a new name'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_out_user_can_edit_profile(self):
        response = self.client.put('/profiles/1/', {
            'name': 'a new name'
        })
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_cannot_retrieve_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestModel(APITestCase):
    def test_model_string_method_return_title(self):
        User.objects.create_user(username='carltest', password='testcarl')
        carltest = User.objects.get(username='carltest')
        response = Profile.objects.get(owner=carltest)
        self.assertEqual(str(response), "carltest's profile")
