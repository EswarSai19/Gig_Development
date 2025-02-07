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
# class Contact(models.Model):
#     name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     reason = models.CharField(max_length=50)
#     description = models.TextField()
#     submitted_at = models.DateTimeField(auto_now_add=True)  # Automatically records submission time

#     def __str__(self):
#         return f"{self.name} ({self.reason})"

def generate_opportunity_id():
    return f"OP{str(uuid.uuid4().int)[:5]}"

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Title: {self.title} with ID {self.opportunityId}"


def generate_freelancer_id():
    return f"FL{str(uuid.uuid4().int)[:8]}"

class Freelancer(models.Model):
    userId = models.CharField(
        primary_key=True, max_length=12, default=generate_freelancer_id, editable=False
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    user_role = models.CharField(max_length=50, default='freelancer')
    profile_summary = models.TextField(max_length=512, blank=True, null=True)
    designation = models.CharField(max_length=50)
    social_media = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=50)
    education = models.CharField(max_length=255)
    certifications = models.CharField(max_length=255, blank=True, null=True)
    experience = models.FloatField()
    skills = models.JSONField(default=dict)  # Example: {"Python": 3.5, "Django": 2.0}
    projects_assigned = models.CharField(max_length=255, blank=True)
    project_status = models.CharField(max_length=50, blank=True)
    profilePic = models.ImageField(upload_to="freelancer/profile_pics/", blank=True, null=True)
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


class Skill(models.Model):
    freelancer = models.ForeignKey(
        Freelancer, 
        on_delete=models.CASCADE, 
        related_name='skill_set'  # Changed related_name to avoid conflict
    )
    skill_name = models.CharField(max_length=100)
    experience_years = models.FloatField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.skill_name} ({self.experience_years} years)"


class Certificate(models.Model):
    freelancer = models.ForeignKey(
        Freelancer, on_delete=models.CASCADE, related_name="certificates"
    )
    certificate_name = models.CharField(max_length=255)  # Name of the certification
    issue_date = models.DateField()  # Date when the certificate was issued
    expiry_date = models.DateField(blank=True, null=True)  # Expiry date (can be null)
    certification_id = models.CharField(max_length=100, unique=True)  # Unique cert ID
    certification_url = models.URLField(blank=True, null=True)  # URL to verify the cert
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.certificate_name} (ID: {self.certification_id})"

# Employment History Model
class EmploymentHistory(models.Model):
    freelancer = models.ForeignKey(
        Freelancer, on_delete=models.CASCADE, related_name="employment_history"
    )
    company = models.CharField(max_length=255)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.job_title}"

def generate_projectquote_id():
    return f"PQ{str(uuid.uuid4().int)[:5]}"

class ProjectQuote(models.Model):
    projectQuoteId = models.CharField(
        primary_key=True, max_length=12, default=generate_projectquote_id, editable=False
    )
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    opportunityId = models.CharField(max_length=20)
    budget = models.CharField(max_length=20)
    time_estimation = models.CharField(max_length=20)  # Days
    comments = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Quote by {self.freelancer.username} for {self.opportunityId}"
