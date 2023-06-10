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


class CustomTaskDetailViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        User.objects.create_user(username='junotest', password='testjuno')
        carltest = User.objects.get(username='carltest')
        CustomTask.objects.create(
            owner=carltest, title='a title',
            due_date='2023-07-01T13:20:30+03:00',
            start_date='2023-07-01T13:20:30+03:00'
        )

    def test_logged_in_user_can_list_custom_task(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('/customtask/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_custom_task_cannot_have_due_date_after_start_date(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put(
            '/customtask/1/', {'title': 'a title',
                               'due_date': '2023-07-01 12:00', 'start_date':
                               '2023-08-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_retrieve_invalid_id(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('customtask/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_out_user_cannnot_list_custom_task(self):
        response = self.client.get('/customtask/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_view_other_user_custom_task(self):
        self.client.login(username='junotest', password='testjuno')
        response = self.client.get('/customtask/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_custom_task_owner_can_edit_own_task(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put(
            '/customtask/1/', {'title': 'a new title',
                               'due_date': '2023-07-01 12:00',
                               'start_date':
                               '2023-07-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_custom_task_owner_cannot_edit_other_user_task(self):
        self.client.login(username='junotest', password='testjuno')
        response_one = self.client.post(
            '/customtask/', {'title': 'a new title',
                             'due_date': '2023-07-01 12:00',
                             'start_date':
                             '2023-07-01 12:00'})
        response_two = self.client.put(
            '/customtask/1/', {'title': 'a new title',
                               'due_date': '2023-07-01 12:00',
                               'start_date':
                               '2023-07-01 12:00'})
        self.assertEqual(response_one.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_two.status_code, status.HTTP_404_NOT_FOUND)

    def test_custom_task_edit_has_valid_dates(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put(
            '/customtask/1/', {'title': 'a title',
                               'due_date': '2023-01-01 12:00', 'start_date':
                               '2023-01-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_custom_task_edit_cannot_have_due_date_after_start_date(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put(
            '/customtask/1/', {'title': 'a title',
                               'due_date': '2023-07-01 12:00', 'start_date':
                               '2023-08-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_custom_task_edit_has_valid_max_date(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put(
            '/customtask/1/', {'title': 'a title',
                               'due_date': '2050-01-01 12:00', 'start_date':
                               '2050-01-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_custom_task_edit_has_valid_title(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put(
            '/customtask/1/', {'title': '',
                               'due_date': '2050-01-01 12:00', 'start_date':
                               '2050-01-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_edit_minus_budget(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.put(
            '/customtask/1/', {'title': 'a title',
                               'due_date': '2023-07-01 12:00', 'start_date':
                               '2023-07-01 12:00', 'budget': '-10'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestModel(APITestCase):
    def test_model_string_method_return_title(self):
        User.objects.create_user(username='carltest', password='testcarl')
        carltest = User.objects.get(username='carltest')
        response = CustomTask.objects.create(
            title='test', due_date='2023-07-01T13:20:30+03:00',
            start_date='2023-07-01T13:20:30+03:00',
            owner=carltest)
        self.assertEqual(str(response), 'test')
