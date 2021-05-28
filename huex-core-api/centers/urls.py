from django.contrib import admin
from django.urls import include, path

from .views import CentersView


urlpatterns = [
    path('center/', CentersView.as_view()),
    path('center/<id>/', CentersView.as_view()),
]