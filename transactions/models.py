import uuid

from django.db import models


class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.CharField(max_length=30)
    date = models.DateField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    time = models.TimeField()
    shop_owner = models.CharField(max_length=14)
    shop = models.CharField(max_length=19)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="transactions"
    )
