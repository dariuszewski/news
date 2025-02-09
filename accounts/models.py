from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(
        null=True, blank=True
    )  # null for db, blank for forms
