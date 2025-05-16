from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


docs_swagger = get_schema_view(
   openapi.Info(
      title="Global Trade API",
      default_version='v0.1',
      description="This is Global Trade API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
