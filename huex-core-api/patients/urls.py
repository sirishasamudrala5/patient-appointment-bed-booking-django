from django.contrib import admin
from django.urls import include, path

from .views import PatientsView


urlpatterns = [
    path('patient/', PatientsView.as_view()),
    path('patient/<id>/', PatientsView.as_view()),
]