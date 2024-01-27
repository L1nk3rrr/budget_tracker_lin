from django.shortcuts import render  # NOQA: F401
from django.views.generic import TemplateView

from transactions.models import Category, Transaction
from wallets.models import Wallet


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_wallet = Wallet.objects.filter(is_default=True).first()
        context["wallets"] = Wallet.objects.order_by("-is_default").all()
        context["wallet_sign"] = default_wallet.currency.sign
        context["wallet_balance"] = default_wallet.get_balance()
        context["categories"] = Category.objects.all()
        context["transactions"] = Transaction.objects.filter(
            wallet=default_wallet.id
        ).all()
        return context
