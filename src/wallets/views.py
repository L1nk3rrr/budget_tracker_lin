from django.urls import reverse_lazy
from django.views.generic import CreateView

from wallets.forms import WalletForm


class CreateWalletView(CreateView):
    template_name = "wallets/create.html"
    form_class = WalletForm
    success_url = reverse_lazy("core:index")

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the current user
        return super().form_valid(form)
