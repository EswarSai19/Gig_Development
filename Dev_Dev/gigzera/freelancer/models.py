from django.db import models
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now
from django.db.models import JSONField
import json
# Create your models here.
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

def generate_opportunity_id():
    return f"OP{str(uuid.uuid4().int)[:6]}"

class ProjectsDisplay(models.Model):

    opportunityId = models.CharField(
        primary_key=True, max_length=12, default=generate_opportunity_id, editable=False
    )
    title = models.CharField(max_length=255)
    budget = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    start_date = models.DateField()
    project_type = models.CharField(max_length=50)
    description = models.TextField()
    deliverables = models.TextField()
    requirements = models.TextField()
    challenges = models.TextField()
    skills_required = models.CharField(max_length=255)
    

    def __str__(self):
        return f"Title: {self.title} with ID {self.opportunityId}"
