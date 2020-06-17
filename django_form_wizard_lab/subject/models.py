from django.db import models
from django.utils.translation import ugettext_lazy as _

from autoslug import AutoSlugField

from model_utils.models import TimeStampedModel

class Subject(TimeStampedModel):
    name =  models.CharField(_("Subject"), max_length=255)
    slug = AutoSlugField(populate_from='name')
    number_sks = models.IntegerField()