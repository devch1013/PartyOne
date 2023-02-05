from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager
import uuid

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError("Users should have a username")
        user = self.model(username=username, email=email)
        user.uuid = uuid.uuid4()
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ("MALE", "남성"),
        ("FEMALE", "여성"),
    )
    email = models.EmailField(max_length=50, unique=True, null=True)
    thumbnail = models.BooleanField(default=False)
    username = models.CharField(max_length=20, unique=True)
    profile_text = models.TextField(max_length=500, blank=True)
    uuid = models.UUIDField(unique=True, null=True)
    notice = models.BooleanField(default=True)
    birth_day = models.DateField(null=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES)

    class Meta:
        db_table = "user"

    USERNAME_FIELD = "username"
    objects = CustomUserManager()

    @staticmethod
    def authenticate(email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            return False
        except:
            return None
