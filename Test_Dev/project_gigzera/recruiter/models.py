import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.timezone import now

# Create your models here.
def generate_recruiter_id():
    return f"RE{str(uuid.uuid4().int)[:10]}"


class Recruiter(models.Model):
    userId = models.CharField(
        primary_key=True, max_length=12, default=generate_recruiter_id, editable=False
    )
    name = models.CharField(max_length=255)
    profilePic = models.ImageField(upload_to="recruiter/profile_pics/", blank=True, null=True)
    phone_number = models.BigIntegerField()
    email_id = models.EmailField(unique=True)
    user_role = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    job_portal_links = ArrayField(models.URLField(), blank=True, default=list)
    designation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    unique_organization_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    opportunity_id = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    password = models.CharField(max_length=128)
    project_status = ArrayField(
        models.CharField(max_length=50, choices=[
            ('inprogress', 'In Progress'),
            ('completed', 'Completed'),
            ('not_started', 'Not Started'),
        ]), blank=True, default=list
    )
    joining_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
