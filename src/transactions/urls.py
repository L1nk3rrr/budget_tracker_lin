from django.urls import path

from transactions.views import (CreateTransactionIndexView,
                                get_transactions_by_wallet)

app_name = "transactions"
urlpatterns = [
    path("create/", CreateTransactionIndexView.as_view(), name="create_transaction"),
    path(
        "by_wallet/<int:wallet_id>",
        get_transactions_by_wallet,
        name="get_transactions_by_wallet",
    ),
]
