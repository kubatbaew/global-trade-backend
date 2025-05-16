from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from core.docs import docs_swagger
from core.admin import main_admin

api_v1_urlpatterns = [
    path("", include("apps.clients.urls")),
]

urlpatterns = [
    path('admin/', main_admin.site.urls),
    path('docs/', docs_swagger.with_ui('swagger', cache_timeout=0)),
    path("api/", include(api_v1_urlpatterns))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
