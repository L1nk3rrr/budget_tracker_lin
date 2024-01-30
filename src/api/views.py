from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response

from api.serializers import (BaseTransactionSerializer, CustomerSerializer,
                             WalletSerializer)
from transactions.models import Transaction
from wallets.models import Wallet


class CustomerCreateAPIView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateAPIView(UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerDestroyAPIView(DestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerListAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class CustomerOneAPIView(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class WalletCreateAPIView(CreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletUpdateAPIView(UpdateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletDestroyAPIView(DestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletListAPIView(ListAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class WalletOneAPIView(RetrieveAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class GetTransactionsByWalletAPIView(ListAPIView):
    def get(self, request, wallet_id):
        try:
            wallet = Wallet.objects.get(pk=wallet_id)
            transactions = Transaction.objects.filter(wallet=wallet)
            serializer = BaseTransactionSerializer(transactions, many=True)
            balance = wallet.get_balance()
            return Response(
                {
                    "transactions": serializer.data,
                    "wallet_balance": balance,
                }
            )
        except Wallet.DoesNotExist:
            return Response(
                {"error": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND
            )


class CreateTransactionAPIView(CreateAPIView):
    def post(self, request):
        serializer = BaseTransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            balance = transaction.wallet.get_balance()
            return Response(
                {
                    "success": True,
                    "transaction": serializer.data,
                    "wallet_balance": balance,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"success": False, "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
