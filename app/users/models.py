from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_TA = models.BooleanField(default=False)
    is_Professor = models.BooleanField(default=False)
    is_Administrative = models.BooleanField(default=False)

