from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords





class Token(models.Model):
    name = models.CharField('Nombre', max_length=255)
    token = models.CharField('Token', max_length=255)
    historical = HistoricalRecords()

    class Meta:
        verbose_name = 'token'
        verbose_name_plural = 'tokens'

    REQUIRED_FIELDS = ['name', 'token']

    def __str__(self):
        return f'{self.name} {self.token}'

# Create your models here.
