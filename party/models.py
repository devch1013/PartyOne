from django.db import models
import uuid
from users.models import User

# Create your models here.


class Party(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host", default=None)
    max_attendees = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "party"
