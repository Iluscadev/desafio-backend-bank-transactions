from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User

from transactions.models import Transaction


class TransactionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        pass

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





