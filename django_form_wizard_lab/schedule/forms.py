from django import forms

from django.utils.translation import ugettext_lazy as _

from django_form_wizard_lab.schedule.models import Schedule

from django_form_wizard_lab.classes.models import Classes


class ScheduleForm(forms.ModelForm):
    classes = forms.ModelChoiceField(queryset=Classes.objects.all(), empty_label=_("Choose Your Classes"))

    class Meta:
        model = Schedule
        fields = ['classes', 'tanggal', 'time_start', 'time_finish']