from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    department = models.CharField(max_length=255, blank=True)
    is_professor = models.BooleanField(default=False)
