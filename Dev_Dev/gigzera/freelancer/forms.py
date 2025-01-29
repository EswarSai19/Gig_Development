from django import forms
from django.forms import inlineformset_factory
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'reason', 'description']




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