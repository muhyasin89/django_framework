from django import forms

from django.utils.translation import ugettext_lazy as _

from django_form_wizard_lab.place.models import Place

from django_form_wizard_lab.classes.models import Classes


class PlaceForm(forms.ModelForm):
    classes = forms.ModelChoiceField(queryset=Classes.objects.all(), empty_label=_("Choose Your Classes"))

    class Meta:
        model = Place
        fields = ['name', 'floor', 'building', 'room', 'classes']