from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import (CreateTransactionAPIView, CustomerCreateAPIView,
                       CustomerDestroyAPIView, CustomerListAPIView,
                       CustomerOneAPIView, CustomerUpdateAPIView,
                       GetTransactionsByWalletAPIView, WalletCreateAPIView,
                       WalletDestroyAPIView, WalletListAPIView,
                       WalletOneAPIView, WalletUpdateAPIView)

app_name = "api"

router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Budget Tracker API",
        default_version="v1.0",
        description="API for budget tracker",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("", include(router.urls)),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("customers/", CustomerListAPIView.as_view(), name="customers_all"),
    path("customers/<int:pk>/", CustomerOneAPIView.as_view(), name="customer_one"),
    path("customers/create/", CustomerCreateAPIView.as_view(), name="customer_create"),
    path(
        "customers/update/<int:pk>/",
        CustomerUpdateAPIView.as_view(),
        name="customer_update",
    ),
    path(
        "customers/delete/<int:pk>/",
        CustomerDestroyAPIView.as_view(),
        name="customer_delete",
    ),
    path("wallets/", WalletListAPIView.as_view(), name="wallets_all"),
    path("wallets/<int:pk>/", WalletOneAPIView.as_view(), name="wallets_one"),
    path("wallets/create/", WalletCreateAPIView.as_view(), name="wallets_create"),
    path(
        "wallets/update/<int:pk>/", WalletUpdateAPIView.as_view(), name="wallets_update"
    ),
    path(
        "wallets/delete/<int:pk>/",
        WalletDestroyAPIView.as_view(),
        name="wallets_delete",
    ),
    path(
        "transactions/by_wallet/<int:wallet_id>/",
        GetTransactionsByWalletAPIView.as_view(),
        name="get_transactions_by_wallet",
    ),
    path(
        "transactions/create",
        CreateTransactionAPIView.as_view(),
        name="create_transaction",
    ),
]
