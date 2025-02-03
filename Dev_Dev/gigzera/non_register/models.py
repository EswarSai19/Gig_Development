import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now
from django.db.models import JSONField
import json


def generate_contact_id():
    return "CN" + str(uuid.uuid4().hex[:4]).upper()

# Create your models here.
class Contact(models.Model):
    contact_id = models.CharField(max_length=10, default=generate_contact_id, primary_key=True)
    user_type = models.CharField(max_length=50, default="Non_register")
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    reason = models.CharField(max_length=50)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically records submission time

    def __str__(self):
        return f"{self.name} ({self.reason})"


