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
            'phone',
            'email',
            'social_media',
            'education',
            'certifications',
            'experience',
            'skills',  # JSONField for skills input
            'password',
        ]
    profilePic = forms.ImageField(required=False)
    # social_media = forms.JSONField(required=False)
    # education = forms.CharField(required=False)
    # certifications = forms.CharField(required=False)
    # experience = forms.IntegerField(required=False)
    # skills = forms.JSONField(required=False)
    projects_assigned = forms.CharField(required=False)
    project_status = forms.CharField(required=False)

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