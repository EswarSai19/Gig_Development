import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
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
    return f"FL{str(uuid.uuid4().int)[:10]}"

# class Freelancer(models.Model):
#     userId = models.CharField(max_length=12, primary_key=True)
#     Name = models.CharField(max_length=255)
#     profilePic = models.TextField(blank=True, null=True)
#     phone = models.BigIntegerField(blank=True, null=True)
#     email = models.EmailField(unique=True)
#     user_role = models.CharField(max_length=50)
#     Country = models.CharField(max_length=100, blank=True, null=True)
#     ProfessionalProfile = models.TextField(blank=True, null=True)
#     JobTitle = models.TextField(blank=True, null=True)
#     Education = models.CharField(max_length=255, blank=True, null=True)
#     UserVerifiedStatus = models.BooleanField(default=False)
#     password = models.CharField(max_length=255)
#     TotalWorkExperience = models.FloatField(blank=True, null=True)
#     ProjectsAssigned = models.JSONField(blank=True, null=True)  # Requires Django 3.1+
#     CreatedAt = models.DateTimeField()
#     UpdatedAt = models.DateTimeField()

#     def __str__(self):
#         return f"{self.userId} - {self.Name}"

#     def get_projects_assigned(self):
#         return json.loads(self.ProjectsAssigned or "[]")  # Parse JSON if necessary

class Freelancer(models.Model):
    userId = models.CharField(
        primary_key=True, max_length=12, default=generate_freelancer_id, editable=False
    )
    name = models.CharField(max_length=255)
    profilePic = models.ImageField(upload_to="freelancer/profile_pics/", blank=True, null=True)
    phone = models.BigIntegerField()
    email = models.EmailField(unique=True)
    user_role = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    social_media = models.URLField(blank=True, null=True)
    education = models.CharField(max_length=255)
    certifications = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    experience = models.FloatField()
    skills = models.JSONField(default=dict)  # Example: {"Python": 3.5, "Django": 2.0}
    password = models.CharField(max_length=128)
    projects_assigned = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    project_status = ArrayField(
        models.CharField(max_length=50, choices=[
            ('inprogress', 'In Progress'),
            ('completed', 'Completed'),
            ('not_started', 'Not Started'),
        ]), blank=True, default=list
    )
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    freelancer = models.ForeignKey(
        Freelancer, 
        on_delete=models.CASCADE, 
        related_name='skill_set'  # Changed related_name to avoid conflict
    )
    skill_name = models.CharField(max_length=100)
    experience_years = models.PositiveIntegerField()

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

    def __str__(self):
        return f"{self.company} - {self.job_title}"