from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeStampedModel

from online_learning.users.models import User

from autoslug import AutoSlugField

import uuid

STATUS = [
    (ACTIVE, 'active'),
    (INACTIVE, 'inactive'),
]


class Student(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(
        max_length=225,
        choices=STATUS,
        default=ACTIVE
    )

    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")


class Student_preference(TimeStampedModel):
    pass
