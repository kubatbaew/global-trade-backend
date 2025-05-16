from django.contrib import admin

from apps.cashbacks.models import CashBack

@admin.register(CashBack)
class CashBackAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'balance']
