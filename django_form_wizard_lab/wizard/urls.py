from django.urls import path

from .views import SemesterWizard

app_name = "wizard"
urlpatterns = [
    path("", SemesterWizard.as_view(), name="form")
]