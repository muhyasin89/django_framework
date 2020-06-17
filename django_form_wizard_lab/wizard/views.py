from django.shortcuts import render

from django.http import HttpResponseRedirect

from django_form_wizard_lab.classes.forms import ClassesForm
from django_form_wizard_lab.place.forms import PlaceForm
from django_form_wizard_lab.subject.forms import SubjectForm
from django_form_wizard_lab.schedule.forms import ScheduleForm
from django_form_wizard_lab.teacher.forms import TeacherForm
from django_form_wizard_lab.student.forms import StudentForm


from formtools.wizard.views import WizardView


def do_something_with_the_form_data(form_list):
    import pdb;pdb.set_trace()

class SemesterWizard(WizardView):
    template_name = "form_wizard/form.html"
    form_list = [ClassesForm, PlaceForm, SubjectForm, ScheduleForm, TeacherForm, StudentForm]

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)


    def done(self, form_list, **kwargs):
        do_something_with_the_form_data(form_list)
        return HttpResponseRedirect('/page-to-redirect-to-when-done/')
