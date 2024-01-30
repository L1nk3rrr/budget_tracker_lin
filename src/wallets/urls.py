from django.urls import path

from wallets.views import CreateWalletView, DeleteWalletView, UpdateWalletView

app_name = "wallets"
urlpatterns = [
    path("create/", CreateWalletView.as_view(), name="create_wallet"),
    path("update/<int:pk>", UpdateWalletView.as_view(), name="update_wallet"),
    path("delete/<int:pk>", DeleteWalletView.as_view(), name="delete_wallet"),
]
