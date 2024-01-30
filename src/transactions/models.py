from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Transaction(BaseModel):
    class TypeChoice(models.IntegerChoices):
        EXPENSE = 0, _("Expense")
        INCOME = 1, _("Income")

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    wallet = models.ForeignKey(
        to="wallets.Wallet", on_delete=models.CASCADE, related_name="transactions"
    )
    category = models.ForeignKey(
        to="transactions.Category",
        on_delete=models.PROTECT,
        related_name="transactions",
    )
    tags = models.ManyToManyField("transactions.Tag")
    type = models.PositiveSmallIntegerField(
        choices=TypeChoice.choices, default=TypeChoice.EXPENSE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type}: {self.category.name} - {self.amount}"


class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    name = models.CharField(max_length=255)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    icon = models.ImageField(upload_to="category_icons/", blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        ordering = ("priority",)

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    color = models.CharField(
        max_length=7, validators=[MinLengthValidator(7)], blank=True
    )
    priority = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(
        to="transactions.Category", on_delete=models.CASCADE, related_name="tags"
    )

    def __str__(self):
        return self.name
