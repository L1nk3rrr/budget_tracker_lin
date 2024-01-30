from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from transactions.models import Transaction


@receiver(pre_delete, sender=Transaction)
def update_card_balance_on_delete(sender, instance, **kwargs):
    instance.wallet.balance -= instance.amount
    instance.wallet.save()


@receiver(post_save, sender=Transaction)
def update_card_balance_on_update(sender, instance, created, **kwargs):
    if created:
        # Update card balance based on transaction amount
        instance.wallet.balance += instance.amount
        instance.wallet.save()
    else:
        difference = instance.amount - instance.previous_amount
        instance.wallet.balance += difference
        instance.wallet.save()
