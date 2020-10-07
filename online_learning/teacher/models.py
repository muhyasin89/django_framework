from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField


class Teacher(TimeStampedModel):
    name = models.CharField(_("Classes"), max_length=255)
    slug = AutoSlugField(populate_from='name')

    address = models.CharField(_("Address"), max_length=255)
    
    years_of_experience = models.IntegerField()


    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")