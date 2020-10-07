from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = CharField(_("First Name"), blank=True, max_length=255)
    last_name = CharField(_("Last Name"), blank=True, max_length=255)
    address = CharField(_("Address"), blank=True, max_length=255)
    phone_number = PhoneNumberField(blank=True)
    birthday = DateField()

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
