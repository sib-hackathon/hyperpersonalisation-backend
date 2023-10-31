from django.db import models
from users.models import User

# Create your models here.

class Button(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name
  
class UserButtonInteraction(models.Model):
  button = models.ForeignKey(Button, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)


class UserAddedButtons(models.Model):
  button = models.ForeignKey(Button, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now_add=True)
