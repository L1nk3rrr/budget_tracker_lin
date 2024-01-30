from django.contrib.auth import get_user_model
from rest_framework.fields import CharField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from transactions.models import Category, Transaction
from wallets.models import Currency, Wallet


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "last_name", "email", "phone_number", "is_staff")


class WalletSerializer(ModelSerializer):
    currency = PrimaryKeyRelatedField(queryset=Currency.objects.all())

    class Meta:
        model = Wallet
        fields = ("id", "name", "currency", "balance", "is_default")


class BaseTransactionSerializer(ModelSerializer):
    wallet_sign = CharField(source="wallet.currency.sign", required=False)
    category_name = CharField(source="category.name", required=False)

    class Meta:
        model = Transaction
        fields = (
            "id",
            "description",
            "category",
            "category_name",
            "amount",
            "wallet",
            "wallet_sign",
            "type",
        )
