from rest_framework import serializers
from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'title', 'message', 'date_created', 'date_updated', 'read']
        read_only_fields = ['id', 'user', 'title', 'message', 'date_created', 'date_updated']
        extra_kwargs = {'read': {'write_only': True}}
