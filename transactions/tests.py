from urllib import response

from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User

from transactions.models import Transaction


class TransactionModelTest(TestCase):
    def test_transaction_creation(self):
        transaction = Transaction.objects.create(
            type= "Financiamento",
            date= "2019-03-01",
            value= "142.00",
            cpf= "09620676017",
            card= "4753****3153",
            time= "15:34:53",
            shop_owner= "JOÃO MACEDO",
            shop= "BAR DO JOÃO"
        )

        self.assertIsNotNone(transaction.id)

    def test_transaction_wrong_fields_creation(self):
        with self.assertRaises(TypeError):
            Transaction.objects.create(
            type= 999,
            date= True,
            value= "142.00",
            cpf= "09620676017",
            card= "4753****3153",
            time= "15:34:53",
            shop_owner= "JOÃO MACEDO",
            shop= "BAR DO JOÃO"
        )


class TransactionViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.transaction = Transaction.objects.create(
            type= "Financiamento",
            date= "2019-03-01",
            value= "142.00",
            cpf= "09620676017",
            card= "4753****3153",
            time= "15:34:53",
            shop_owner= "JOÃO MACEDO",
            shop= "BAR DO JOÃO"
        )

        user = User.objects.create_user(
            username="user",
            password="1234"
        )

        cls.token = Token.objects.create(user=user)

        cls.retrieveUrl = reverse("retrieve", kwargs={"transaction_id": cls.transaction.id})
        
        cls.listUrl = reverse("list")

    def test_list_transactions(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        response = self.client.get(self.listUrl)

        expected_status_code = status.HTTP_200_OK

        self.assertEqual(expected_status_code, response.status_code)

    def test_unauthorized_list_transactions(self):
        response = self.client.get(self.listUrl)

        expected_status_code = status.HTTP_401_UNAUTHORIZED

        self.assertEqual(expected_status_code, response.status_code)

    def test_retrieve_transaction(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        response = self.client.get(self.retrieveUrl)

        expected_status_code = status.HTTP_200_OK

        self.assertEqual(expected_status_code, response.status_code)

    def test_unauthorized_retrieve_transaction(self):
        response = self.client.get(self.retrieveUrl)

        expected_status_code = status.HTTP_401_UNAUTHORIZED

        self.assertEqual(expected_status_code, response.status_code)


