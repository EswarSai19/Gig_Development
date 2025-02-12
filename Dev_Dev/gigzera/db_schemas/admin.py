from django.contrib import admin
from .models import Contact, Client, ProjectsDisplay, Freelancer, Skill, Certificate, EmploymentHistory, ProjectStatusDetails
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'reason', 'description', 'submitted_at')
    search_fields = ('name', 'email', 'reason')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('userId', 'name', 'email', 'phone', 'user_role', 'country', 'company', 'designation' )
    search_fields = ('name', 'email', 'userId', 'phone', 'company')

@admin.register(ProjectStatusDetails)
class ProjectStatusDetailsAdmin(admin.ModelAdmin):
    list_display = ('opportunity_id', 'freelancer_id', 'status', 'progress')
    search_fields = ('opportunity_id', 'freelancer_id', 'status', 'progress')

@admin.register(ProjectsDisplay)
class ProjectsDisplayAdmin(admin.ModelAdmin):
    list_display = ('opportunityId', 'title', 'budget', 'duration', 'time_zone', 'start_date', 'project_type', 'description','deliverables','requirements','challenges','skills_required')
    search_fields = ('opportunityId', 'title', 'project_type', 'skills_required')

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('userId', 'name', 'email', 'user_role', 'country')
    search_fields = ('name', 'email', 'userId')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'skill_name', 'experience_years')
    search_fields = ('skill_name',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'certificate_name', 'issue_date', 'expiry_date', 'certification_id', 'certification_url')
    search_fields = ('certificate_name', 'certification_id')

@admin.register(EmploymentHistory)
class EmploymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('freelancer', 'company', 'job_title', 'start_date', 'end_date')
    search_fields = ('company', 'job_title')

