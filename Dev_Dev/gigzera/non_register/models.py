import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now
from django.db.models import JSONField
import json

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    reason = models.CharField(max_length=50)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically records submission time

    def __str__(self):
        return f"{self.name} ({self.reason})"

def generate_freelancer_id():
    return "FL" + str(uuid.uuid4().hex[:10]).upper()
    
def generate_opportunity_id():
    return f"OP{str(uuid.uuid4().int)[:5]}"