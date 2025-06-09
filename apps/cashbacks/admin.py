from django.contrib import admin

from apps.cashbacks.models import CashbackBalance, CashbackTransaction


@admin.register(CashbackBalance)
class CashbackBalanceAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(CashbackTransaction)
class CashbackBalanceAdmin(admin.ModelAdmin):
    list_display = ['user']