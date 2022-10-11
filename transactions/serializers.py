from rest_framework.serializers import ModelSerializer

from transactions.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "type", "date", "value", "cpf", "card", "time", "shop_owner", "shop"]
        read_only_fields = ["id", "user_id"]


    