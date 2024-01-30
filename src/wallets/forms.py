from django.forms import ModelForm, widgets

from wallets.models import Wallet


class BaseWalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = (
            "name",
            "currency",
            "balance",
            "is_default",
        )
