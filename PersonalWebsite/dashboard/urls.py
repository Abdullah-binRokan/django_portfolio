from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard_projects_view, name="dashboard_projects_view"),
    path("messages/", views.dashboard_messages_view, name="dashboard_messages_view"),
]