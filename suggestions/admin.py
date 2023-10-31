from django.contrib import admin
from suggestions.models import Button

class ButtonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Button, ButtonAdmin)
