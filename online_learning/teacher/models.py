from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel
from online_learning.users.models import User

from autoslug import AutoSlugField

import uuid

class Teacher(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    goal = models.TextField()

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")
