from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.http import require_http_methods

from transactions.forms import TransactionForm
from transactions.models import Transaction
from wallets.models import Wallet


class CreateTransactionIndexView(View):
    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save()  # Assuming TransactionForm handles saving
            # Serialize transaction data for JSON response
            serialized_data = transaction.serialize()

            return JsonResponse(
                {
                    "success": True,
                    "transaction": serialized_data,
                    "wallet_balance": transaction.wallet.get_balance(),
                }
            )
        else:
            errors = {key: value for key, value in form.errors.items()}
            return JsonResponse({"success": False, "errors": errors})


@require_http_methods(
    [
        "GET",
    ]
)
def get_transactions_by_wallet(request, wallet_id):
    try:
        wallet = get_object_or_404(Wallet, pk=wallet_id)
        transactions = Transaction.objects.filter(wallet=wallet)
        balance = wallet.get_balance()
        sign = wallet.currency.sign
        return JsonResponse(
            {
                "transactions": list(
                    transaction.serialize() for transaction in transactions
                ),
                "wallet_balance": balance,
                "wallet_sign": sign,
            }
        )
    except Wallet.DoesNotExist:
        return JsonResponse({"error": "Wallet not found"}, status=404)
