from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from users.models import User, GeneralSettings
from notifications.models import Notification

class Command(BaseCommand):
    help = 'Sends an e-mail reminder to users with e_lock enabled'

    def handle(self, *args, **kwargs):
        print("Running the server")
        users_with_elock = GeneralSettings.objects.filter(e_lock_enabled=True).select_related('user')
        for setting in users_with_elock:
            notification = Notification.objects.create(
                user=setting.user,
                title="E-Lock Enabled",
                message="You have enabled the E-Lock for a while and has not been disabled. Please disable it if you are done using it.",
            )
            notification.save()