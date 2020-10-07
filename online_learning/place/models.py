from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField

from online_learning.classes.models import Classes


class Place(TimeStampedModel):
    name =  models.CharField(_("Classes"), max_length=255)
    slug = AutoSlugField(populate_from='name')

    building = models.CharField(_("Building"), max_length=255)

    floor = models.IntegerField()

    room = models.CharField(_("Room"), max_length=255)

    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("place")
        verbose_name_plural = _("places")