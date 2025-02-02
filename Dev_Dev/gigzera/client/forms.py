from django import forms
from django.forms import inlineformset_factory
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'reason', 'description']
