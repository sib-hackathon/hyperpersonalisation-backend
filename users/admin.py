from django.contrib import admin
from users.models import User, GeneralSettings

class SettingsInline(admin.TabularInline):
    model = GeneralSettings

    def has_delete_permission(self, request, obj=None):    
      return False


@admin.register(User)
class Users(admin.ModelAdmin):
    inlines = (SettingsInline, )
