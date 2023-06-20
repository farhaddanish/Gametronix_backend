from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class AccountsManager (BaseUserManager):
    def create_user(self, first_name, last_name, email, password):
        if not email:
            raise ValueError("User must have an email address")

        if not password:
            raise ValueError("User must have a username")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email.lower()),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Accounts (AbstractBaseUser):
    USERNAME_FIELD = "email"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    live_strem = models.IntegerField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to="accounts/profile", blank=True)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = AccountsManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
    



    class Meta:
        verbose_name_plural = "Accounts"
