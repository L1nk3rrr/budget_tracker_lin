from django.urls import path

from wallets.views import CreateWalletView

app_name = "wallets"
urlpatterns = [
    path("create/", CreateWalletView.as_view(), name="create_wallet"),
]
