from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http.request import HttpRequest
from users.models import User, GeneralSettings

class SettingsInline(admin.TabularInline):
    model = GeneralSettings
    extra = 1

    def has_delete_permission(self, request, obj=None):    
      return False

class CustomUserAdmin(UserAdmin):
    inlines = [SettingsInline]

    list_display = ('email', 'name', 'phone', 'date_of_birth', 'account_type', 'balance', 'date_opened', 'branch_number', 'created_at', 'is_active')
    list_filter = ('account_type', 'is_active', 'is_staff')
    search_fields = ('email', 'name', 'phone')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone', 'date_of_birth')}),
        ('Account Info', {'fields': ('account_type', 'balance', 'date_opened', 'branch_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions')})  # Include 'groups' and 'user_permissions' fields
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'phone', 'date_of_birth', 'account_type', 'balance', 'date_opened', 'branch_number', 'is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions')  # Include 'groups' and 'user_permissions' fields
        }),
    )

admin.site.register(User, CustomUserAdmin)