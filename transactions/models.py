from django.db import models
from users.models import User
import uuid
# Create your models here.

class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    payed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payed_by')
    payed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payed_to')
    amount = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.payed_by) + ' - ' + str(self.amount) + ' - ' + str(self.is_completed)