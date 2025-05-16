from django.contrib import admin

from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    search_fields = ['username']

    exclude = [
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "email",
        "user_permissions",
        "groups"
    ]
