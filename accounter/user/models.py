from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('firt name'),max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Photo(models.Model):
    photo = models.ImageField(
        upload_to="image/expenses/%Y/%m/%d/",
    )

    def __str__(self):
        return f"{self.id}, path-{self.photo}"

    class Meta:
        verbose_name = "photo"
        verbose_name_plural ="photos"