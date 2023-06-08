from django.contrib.auth.models import User
from .models import Holiday
from rest_framework import status
from rest_framework.test import APITestCase


class HolidayListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='carltest', password='testcarl')
        carltest = User.objects.get(username='carltest')
        Holiday.objects.create(
            owner=carltest, title='a title', date_of_holiday='2023-07-01 12:00'
            )

    def test_can_list_holiday_tasks(self):
        response = self.client.get('/holiday/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_list_holiday_tasks(self):
        self.client.login(username='carltest', password='testcarl')
        response = self.client.get('/holiday/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
