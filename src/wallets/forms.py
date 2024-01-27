from django.forms import ModelForm

from wallets.models import Wallet


class WalletForm(ModelForm):
    class Meta:
        model = Wallet
        fields = (
            "name",
            "currency",
        )

    @staticmethod
    def normalize_text(text: str) -> str:
        return text.strip().capitalize()
