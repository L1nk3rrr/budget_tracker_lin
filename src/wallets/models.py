from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Wallet(BaseModel):
    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")

    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        to=get_user_model(), on_delete=models.CASCADE, related_name="wallets"
    )
    currency = models.ForeignKey(
        to="wallets.Currency", on_delete=models.SET_NULL, null=True
    )
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.currency.short_name}"

    def get_balance(self):
        return "%.2f" % self.balance


class Currency(BaseModel):
    class Meta:
        verbose_name = _("Currency")
        verbose_name_plural = _("Currencies")

    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=3)
    sign = models.CharField(max_length=1, default="$")

    def __str__(self):
        return f"{self.name} {self.sign}"
