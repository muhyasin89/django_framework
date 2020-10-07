from django import forms

from django.utils.translation import ugettext_lazy as _

from online_learning.subject.models import Subject


class SubjectForm(forms.ModelForm):
    
    class Meta:
        model = Subject
        fields = ['name', 'number_sks']