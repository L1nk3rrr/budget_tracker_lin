from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from wallets.forms import BaseWalletForm
from wallets.models import Wallet


class CreateWalletView(LoginRequiredMixin, CreateView):
    template_name = "wallets/create.html"
    form_class = BaseWalletForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user
        return super().form_valid(form)


class UpdateWalletView(LoginRequiredMixin, UpdateView):
    template_name = "wallets/update.html"
    form_class = BaseWalletForm
    queryset = Wallet.objects.all()
    success_url = reverse_lazy("core:index")


class DeleteWalletView(LoginRequiredMixin, DeleteView):
    template_name = "wallets/delete.html"
    queryset = Wallet.objects.all()
    success_url = reverse_lazy("core:index")
