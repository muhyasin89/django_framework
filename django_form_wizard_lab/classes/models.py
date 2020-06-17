from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from autoslug import AutoSlugField


class Classes(TimeStampedModel):
    name =  models.CharField(_("Classes"), max_length=255)
    slug = AutoSlugField(populate_from='name')