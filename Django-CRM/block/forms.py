from dataclasses import fields
from django import forms
from .models import LeadRegister


class Registration(forms.ModelForm):
    class Meta:
        model = LeadRegister
        fields = (
            'first_name',
            'last_name',
            'email',
        )