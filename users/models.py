from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=20)
    age = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
