
# Create your models here.
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField
from django.utils.timezone import now
from django.db.models import JSONField



def generate_freelancer_id():
    return f"FL{str(uuid.uuid4().int)[:10]}"


# class Freelancer(models.Model):
#     userId = models.CharField(
#         primary_key=True, max_length=12, default=generate_freelancer_id, editable=False
#     )
#     name = models.CharField(max_length=255)
#     profilePic = models.ImageField(upload_to="freelancer/profile_pics/", blank=True, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(unique=True)
#     user_role = models.CharField(max_length=50)
#     country = models.CharField(max_length=100)
#     social_media = models.URLField(blank=True, null=True)
#     education = models.CharField(max_length=255)
#     certifications = ArrayField(models.CharField(max_length=255), blank=True, default=list)
#     experience = models.FloatField()
#     skills = models.JSONField(default=dict)  # Example: {"Python": 3.5, "Django": 2.0}
#     password = models.CharField(max_length=128)
#     projects_assigned = ArrayField(models.CharField(max_length=255), blank=True, default=list)
#     project_status = ArrayField(
#         models.CharField(max_length=50, choices=[
#             ('inprogress', 'In Progress'),
#             ('completed', 'Completed'),
#             ('not_started', 'Not Started'),
#         ]), blank=True, default=list
#     )
#     created_at = models.DateTimeField(default=now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Skill(models.Model):
#     freelancer = models.ForeignKey(
#         Freelancer, 
#         on_delete=models.CASCADE, 
#         related_name='skill_set'  # Changed related_name to avoid conflict
#     )
#     skill_name = models.CharField(max_length=100)
#     experience_years = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.skill_name} ({self.experience_years} years)"












# class Freelancer(models.Model):
#     userId = models.CharField(
#         primary_key=True, max_length=12, default=generate_freelancer_id, editable=False
#     )
#     name = models.CharField(max_length=255)
#     profilePic = models.ImageField(upload_to="freelancer/profile_pics/", blank=True, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(unique=True)
#     user_role = models.CharField(max_length=50)
#     country = models.CharField(max_length=100)
#     social_media = models.URLField(blank=True, null=True)
#     education = models.CharField(max_length=255)
#     certifications = ArrayField(models.CharField(max_length=255), blank=True, default=list)
#     experience = models.FloatField()
#     skills = models.JSONField(default=dict)  # Example: {"Python": 3.5, "Django": 2.0}
#     password = models.CharField(max_length=128)
#     projects_assigned = ArrayField(models.CharField(max_length=255), blank=True, default=list)
#     project_status = ArrayField(
#         models.CharField(max_length=50, choices=[
#             ('inprogress', 'In Progress'),
#             ('completed', 'Completed'),
#             ('not_started', 'Not Started'),
#         ]), blank=True, default=list
#     )
#     created_at = models.DateTimeField(default=now)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# class Skill(models.Model):
#     freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE, related_name='skills')
#     skill_name = models.CharField(max_length=100)
#     experience_years = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.skill_name} ({self.experience_years} years)"


