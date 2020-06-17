from django import forms

from django.utils.translation import ugettext_lazy as _

from django_form_wizard_lab.teacher.models import Teacher


class TeacherForm(forms.ModelForm):
    
    class Meta:
        model = Teacher
        fields = ['name', 'address', 'years_of_experience']