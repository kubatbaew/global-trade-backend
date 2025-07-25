from rest_framework.routers import DefaultRouter

from apps.cashbacks.views import GetCashBackBalance, CashbackTransactionListAPIViewSet, CashbackTransactionViewSet, CashBackTransactionAllListAPIView

router = DefaultRouter()

router.register("balance", GetCashBackBalance)
router.register("transaction", CashbackTransactionListAPIViewSet, basename="cashback_transaction_list_client")
router.register("transaction_actions", CashbackTransactionViewSet, basename="cashback_transaction_actions")
router.register("transaction/all", CashBackTransactionAllListAPIView, basename="cashback_transaction_all")

urlpatterns = router.urls
