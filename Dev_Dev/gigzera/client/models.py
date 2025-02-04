import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now
from django.db.models import JSONField
import json
# Create your models here.


# class Contact(models.Model):
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     reason = models.CharField(max_length=50)
#     description = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically records submission time

#     def __str__(self):
#         return f"{self.name} ({self.reason})"


def generate_client_id():
    return f"CL{str(uuid.uuid4().int)[:8]}"

class Client(models.Model):
    userId = models.CharField(
        primary_key=True, max_length=12, default=generate_client_id, editable=False
    )
    name = models.CharField(max_length=255)
    profilePic = models.ImageField(upload_to="freelancer/profile_pics/", blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    user_role = models.CharField(max_length=50, default='client')
    country = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    social_media = models.URLField(blank=True, null=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """Hash the password before saving the freelancer."""
        if not self.password.startswith("pbkdf2_sha256$"):  # Avoid re-hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """Verify the password."""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name
