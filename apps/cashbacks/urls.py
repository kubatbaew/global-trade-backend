from rest_framework.routers import DefaultRouter

from apps.cashbacks.views import GetCashBackBalance, CashbackTransactionListAPIViewSet, CashbackTransactionViewSet

router = DefaultRouter()

router.register("balance", GetCashBackBalance)
router.register("transaction", CashbackTransactionListAPIViewSet, basename="cashback_transaction_list_client")
router.register("transaction_actions", CashbackTransactionViewSet, basename="cashback_transaction_actions")

urlpatterns = router.urls
