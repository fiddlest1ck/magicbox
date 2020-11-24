from django.contrib.auth.models import (AbstractBaseUser)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from users.managers import UserManager


class User(AbstractBaseUser):
    class Meta:
        verbose_name = _('Użytkownik')
        verbose_name_plural = _('Użytkownicy')

    CLIENT = 'client'
    SALESMAN = 'salesman'
    SUPERUSER = 'superuser'

    TYPES = (
        (CLIENT, _('klient')),
        (SALESMAN, _('sprzedawca')),
        (SUPERUSER, _('administrator')))

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=32, blank=True)
    last_name = models.CharField(_('last name'), max_length=128, blank=True)
    is_active = models.BooleanField(_('active'), default=False)
    user_type = models.CharField(
        _('typ'), max_length=16, choices=TYPES, default=CLIENT)

    objects = UserManager()

    def __str__(self):
        return getattr(self, self.USERNAME_FIELD, '')

    @property
    def is_staff(self):
        return self.user_type == User.SUPERUSER

    @property
    def is_client(self):
        return self.user_type == User.CLIENT

    @property
    def is_superuser(self):
        return self.user_type == User.SUPERUSER

    @property
    def is_salesman(self):
        return self.user_type == User.SALESMAN

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
