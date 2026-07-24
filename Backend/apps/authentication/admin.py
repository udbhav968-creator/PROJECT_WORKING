from django.contrib import admin
from apps.authentication.models import RoleModel, UserProfileModel


@admin.register(RoleModel)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'is_deleted')
    search_fields = ('name',)
    list_filter = ('is_deleted',)


@admin.register(UserProfileModel)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'role', 'is_active', 'is_deleted', 'created_at')
    search_fields = ('email', 'full_name')
    list_filter = ('is_active', 'is_deleted', 'role')
