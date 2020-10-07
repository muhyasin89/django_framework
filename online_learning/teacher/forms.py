from django import forms

from django.utils.translation import ugettext_lazy as 

from online_learning.teacher.models import Teacher


class TeacherForm(forms.ModelForm):
    
    class Meta:
        model = Teacher
        fields = ['name', 'address', 'years_of_experience']