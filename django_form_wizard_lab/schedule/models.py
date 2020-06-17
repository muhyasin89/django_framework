from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from django_form_wizard_lab.classes.models import Classes


class Schedule(TimeStampedModel):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)

    tanggal = models.DateField()

    time_start = models.TimeField()

    time_finish = models.TimeField()

    class Meta:
        verbose_name = _("schedule")
        verbose_name_plural = _("schedules")