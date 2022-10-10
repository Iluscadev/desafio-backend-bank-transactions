from asyncore import read

import ipdb
from rest_framework.serializers import ModelSerializer
from rest_framework.views import Request, Response, status

from transactions.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "type", "date", "value", "cpf", "card", "time", "shop_owner", "shop", "user_id"]
        read_only_fields = ["id", "user_id"]


    