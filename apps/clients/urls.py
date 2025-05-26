from rest_framework.routers import DefaultRouter

from apps.clients.views import ClientListAPIViewSet


router = DefaultRouter()

router.register("clients", ClientListAPIViewSet)

urlpatterns = router.urls
