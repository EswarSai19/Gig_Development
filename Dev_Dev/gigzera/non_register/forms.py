from django import forms
from django.forms import inlineformset_factory
from .models import Freelancer, Skill, Certificate, Contact, EmploymentHistory

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'reason', 'description']


# Main form for Freelancer
class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = [
            'name',
            'profilePic',
            'phone',
            'email',
            'user_role',
            'country',
            'social_media',
            'education',
            'certifications',
            'experience',
            'skills',  # JSONField for skills input
            'password',
            'projects_assigned',
            'project_status',
        ]

# Inline formsets for related models
SkillFormSet = inlineformset_factory(
    Freelancer,  # Parent model
    Skill,  # Related model
    fields=('skill_name', 'experience_years'),
    extra=1,  # Number of empty forms to display
    can_delete=True,  # Allow deleting skills
)

CertificateFormSet = inlineformset_factory(
    Freelancer,  # Parent model
    Certificate,  # Related model
    fields=('certificate_name', 'issue_date', 'expiry_date', 'certification_id', 'certification_url'),
    extra=1,  # Number of empty forms to display
    can_delete=True,  # Allow deleting certificates
)

class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = [
            'freelancer',
            'company',
            'job_title',
            'description',
            'city',
            'country',
            'start_date',
            'end_date',
            'currently_working',
        ]