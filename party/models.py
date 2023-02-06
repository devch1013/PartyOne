from django.db import models
import uuid
from users.models import User

# Create your models here.


class Party(models.Model):
    id = models.AutoField(primary_key=True)
    col = models.CharField(max_length=10, unique=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    location = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="host", default=None)
    max_attendees = models.IntegerField(default=4)
    longitude = models.CharField(max_length=10, null=True)
    latitude = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "party"


class PartyMemberMapper(models.Model):
    USER_AUTH = ("MEMBER", "member")
    id = models.AutoField(primary_key=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="party")
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member")
    user_auth = models.CharField(max_length=10, default="MEMBER")
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "party_member_mapper"
