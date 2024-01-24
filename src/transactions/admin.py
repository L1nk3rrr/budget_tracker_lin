from django.contrib import admin

from transactions.models import Category, Tag, Transaction

admin.site.register(Transaction)
admin.site.register(Tag)
admin.site.register(Category)
