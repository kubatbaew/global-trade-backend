from rest_framework.routers import DefaultRouter

from apps.cashbacks.views import GetCashBackBalance, CashbackTransactionListAPIViewSet

router = DefaultRouter()

router.register("balance", GetCashBackBalance)
router.register("transaction", CashbackTransactionListAPIViewSet, basename="cashback_transaction_list_client")


urlpatterns = router.urls
