from django.contrib.auth.models import User
from .models import CustomTask
from rest_framework import status
from rest_framework.test import APITestCase


class CustomTaskListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        carltest = User.objects.get(username='carltest')

    def test_can_list_custom_tasks(self):
        response = self.client.get('/customtask/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_list_custom_tasks(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('/customtask/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_custom_task(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post(
            '/customtask/', {'title': 'a title',
                             'due_date': '2023-07-01 12:00', 'start_date':
                             '2023-07-01 12:00'})
        count = CustomTask.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_cannot_create_custom_task(self):
        response = self.client.post(
            '/customtask/', {'title': 'a title',
                             'due_date': '2023-07-01 12:00', 'start_date':
                             '2023-07-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_custom_task_has_valid_dates(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post(
            '/customtask/', {'title': 'a title',
                             'due_date': '2023-01-01 12:00', 'start_date':
                             '2023-01-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_custom_task_has_valid_max_date(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post(
            '/customtask/', {'title': 'a title',
                             'due_date': '2050-01-01 12:00', 'start_date':
                             '2050-01-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_has_valid_title(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post(
            '/customtask/', {'title': '',
                             'due_date': '2023-07-01 12:00', 'start_date':
                             '2023-07-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_minus_budget(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post(
            '/customtask/', {'title': 'a title',
                             'due_date': '2023-07-01 12:00', 'start_date':
                             '2023-07-01 12:00', 'budget': '-10'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
