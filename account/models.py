from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Profile(AbstractUser):
    phone = models.CharField(max_length=13, null=True, blank=True)    
    address = models.TextField(_("address"), null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'