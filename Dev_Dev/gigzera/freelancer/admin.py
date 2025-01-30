from django.contrib import admin
from .models import Contact, ProjectsDisplay
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'reason', 'description', 'submitted_at')
    search_fields = ('name', 'email', 'reason')

@admin.register(ProjectsDisplay)
class ProjectsDisplayAdmin(admin.ModelAdmin):
    list_display = ('opportunityId', 'title', 'budget', 'duration', 'time_zone', 'start_date', 'project_type', 'description','deliverables','requirements','challenges','skills_required')
    search_fields = ('opportunityId', 'title', 'project_type', 'skills_required')

    