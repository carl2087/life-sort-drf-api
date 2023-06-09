from django.contrib.auth.models import User
from .models import Holiday
from rest_framework import status
from rest_framework.test import APITestCase


class HolidayListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        carltest = User.objects.get(username='carltest')

    def test_can_list_holiday_tasks(self):
        response = self.client.get('/holiday/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_list_holiday_tasks(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('/holiday/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_holiday_task(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post('/holiday/', {'title': 'a title',
                                    'date_of_holiday': '2023-07-01 12:00'})
        count = Holiday.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_cannot_create_holiday_task(self):
        response = self.client.post('/holiday/', {'title': 'a title',
                                    'date_of_holiday': '2023-07-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_holiday_task_has_valid_date(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post('/holiday/', {'title': 'a title',
                                    'date_of_holiday': '2023-06-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_has_valid_title(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post('/holiday/', {'title': '',
                                    'date_of_holiday': '2023-07-01 12:00'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_create_minus_budget(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.post(
            '/holiday/', {'title': 'a title', 'date_of_holiday':
                          '2023-07-01 12:00', 'budget': '-10'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class HolidayDetailViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        User.objects.create_user(username='junotest', password='testjuno')
        carltest = User.objects.get(username='carltest')

    def test_logged_in_user_can_list_holiday_task(self):
        self.client.login(username='carltest', password='testcarl')
        self.client.post(
            '/holiday/', {'title': 'a title',
                          'date_of_holiday': '2023-07-01 12:00'})
        response = self.client.get('/holiday/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_can_list_holiday_task(self):
        self.client.login(username='carltest', password='testcarl')
        self.client.post(
            '/holiday/', {'title': 'a title',
                          'date_of_holiday': '2023-07-01 12:00'})
        self.client.logout()
        response = self.client.get('/holiday/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_view_other_user_holiday_task(self):
        self.client.login(username='carltest', password='testcarl')
        self.client.post(
            '/holiday/', {'title': 'a title',
                          'date_of_holiday': '2023-07-01 12:00'})
        self.client.logout()
        self.client.login(username='junotest', password='testjuno')
        response = self.client.get('/holiday/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
