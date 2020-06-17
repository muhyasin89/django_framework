from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField

from django_form_wizard_lab.subject.models import Subject


class Classes(TimeStampedModel):
    name =  models.CharField(_("Classes"), max_length=255)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = _("classes")
        verbose_name_plural = _("classess")


class ClassSubject(TimeStampedModel):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("class")
        verbose_name_plural = _("class_subjects")