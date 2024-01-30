from django.forms import ModelForm

from transactions.models import Transaction


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = (
            "wallet",
            "category",
            "type",
            "amount",
            "description",
        )
