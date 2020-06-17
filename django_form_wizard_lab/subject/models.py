from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField

class Subject(TimeStampedModel):
    name =  models.CharField(_("Subject"), max_length=255)
    slug = AutoSlugField(populate_from='name')
    number_sks = models.IntegerField()


    class Meta:
        verbose_name = _("subject")
        verbose_name_plural = _("subjects")