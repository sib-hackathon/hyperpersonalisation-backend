from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager,PermissionsMixin
import uuid


class UserManager(BaseUserManager):
  """
  Custom Django User Manager for the Custom User Model Created.
  """
  def create_user(self, email, name, phone,password=None, *args, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            *args, **kwargs
        )
        user.set_password(password)  # This line sets the hashed password.
        user.save(using=self._db)
        return user


  def create_superuser(self, email,name,phone,password=None, *args, **kwargs):
      user = self.create_user(
          email=email,
          password=password,
          name = name,
          phone = phone,
          *args, **kwargs
      )
      user.is_admin = True
      user.is_staff = True
      user.save(using=self._db)
      return user


class User(AbstractBaseUser,PermissionsMixin):
  """
  Custom Django User Model without Username.
  """

  ACCOUNT_TYPES = [
      ('SAV', 'Savings'),
      ('CHK', 'Checking'),
      ('BUS', 'Business'),
      ('JNT', 'Joint'),
  ]


  id = models.CharField(max_length=200, default=uuid.uuid4,unique=True,primary_key=True)
  email = models.EmailField(null=False, max_length=100,unique=True)
  name = models.CharField(null=False, max_length=100)
  phone = models.IntegerField(null=False,unique=True)
  date_of_birth = models.DateField()
  account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPES)
  balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  date_opened = models.DateField()
  branch_number = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now=True)


  is_admin = models.BooleanField(default = False)
  is_active = models.BooleanField(default = True)
  is_staff = models.BooleanField(default = False)
  is_superuser = models.BooleanField(default = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name','phone', 'date_of_birth', 'account_type', 'balance', 'date_opened', 'branch_number']

  objects = UserManager()

  def __str__(self):
      return self.name


  def has_perm(self, perm, obj=None):
      return self.is_admin
  
  def has_module_perms(self, app_label):
      return True

  @property
  def account_number(self):
     return self.id
  
  @property
  def age(self):
    import datetime
    return int((datetime.date.today() - self.date_of_birth).days / 365.25 )
  

  def debit(self, amount):
    if self.check_balance(amount):
        self.balance -= amount
        self.save()
        return True
    return False
 
  def credit(self, amount):
    self.balance += amount
    self.save()
    return True

  def check_balance(self, amount):
    if (self.balance - 500) >= amount:
        return True
    return False
  

class GeneralSettings(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   e_lock_enabled = models.BooleanField(default=False)
   e_lock_enabled_date = models.DateTimeField(auto_now_add=True)
   e_lock_updated_date = models.DateTimeField(auto_now=True)
   account_debit_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True)

   def __str__(self):
      return self.user.name