from django.urls import path
from notifications.views import NotificationList, NotificationUpdate

urlpatterns = [
    path('', NotificationList.as_view(), name='notification-list'),
    path('<str:id>/', NotificationUpdate.as_view(), name='notification-update'),
]
