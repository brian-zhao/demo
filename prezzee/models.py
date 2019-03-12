from django.conf import settings
from django.db import models


class GiftCard(models.Model):
    card_value = models.DecimalField(max_digits=10, decimal_places=2)
    voucher_number = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=200)
    archived = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
