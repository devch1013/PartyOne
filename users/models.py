from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    thumbnail = models.BooleanField(default=False)
    username = models.CharField(max_length=20, unique=True)
    profile_text = models.TextField(max_length=500, blank=True)
    uuid = models.UUIDField(unique=True, null=True)
    notice = models.BooleanField(default=True)

    class Meta:
        db_table = "user"

    USERNAME_FIELD = "username"
