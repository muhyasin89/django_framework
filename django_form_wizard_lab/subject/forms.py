from django import forms

from django.utils.translation import ugettext_lazy as _

from django_form_wizard_lab.subject.models import Subject


class SubjectForm(forms.ModelForm):
    
    class Meta:
        model = Subject
        fields = ['name', 'number_sks']