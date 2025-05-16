from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from core.docs import docs_swagger


urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', docs_swagger.with_ui('swagger', cache_timeout=0)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
