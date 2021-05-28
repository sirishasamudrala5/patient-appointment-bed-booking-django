from django.urls import path

from .views import Index, Users, UserEvents, Reports

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('users/', Users.as_view(), name="users"),
    path('users/<id>/', UserEvents.as_view() , name="user_events"),
    path('reports/<year>-<month>/', Reports.as_view() , name="reports")
]