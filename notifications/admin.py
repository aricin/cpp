from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')

admin.site.register(Notification, NotificationAdmin)