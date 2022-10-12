from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from transactions.models import Transaction

from users.models import User


class TransactionModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(
            username= "user",
            email= "mail@mail.com",
            password= "1234",
        )

        self.assertIsNotNone(user.id)


class UserViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create_user(
            username="user0",
            password="1234"
        )
        cls.loginUrl = reverse("login")
        cls.createUrl = reverse("create")

    def test_user_creation(self):
        response = self.client.post(self.createUrl, data={
            "username": "user",
            "password": "1234"
        })
        
        expected_status_code = status.HTTP_201_CREATED

        self.assertEqual(expected_status_code, response.status_code)

    def test_user_login(self):
        response = self.client.post(self.loginUrl, data={
            "username": "user0",
            "password": "1234"
        })
        
        response_data = response.content.decode("utf-8")

        expected_status_code = status.HTTP_200_OK

        self.assertEqual(expected_status_code, response.status_code)
        self.assertTrue(response_data[0])
