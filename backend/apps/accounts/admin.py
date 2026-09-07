from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ProviderProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "username", "role", "is_active", "date_joined")
    list_filter = ("role", "is_active")


@admin.register(ProviderProfile)
class ProviderProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "category", "city", "is_validated")
    list_filter = ("category", "is_validated")