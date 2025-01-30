from django import forms
from .models import ContactBase


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactBase
        fields = ['name', 'mail', 'subject', 'message'] 