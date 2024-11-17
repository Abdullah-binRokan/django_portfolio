from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("about/", views.about_view, name="about_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("delete_contact_msg/<contact_msg_id>/", views.delete_contact_msg_view, name="delete_contact_msg_view"),
    path("add_project/", views.add_project_view, name="add_project_view"),
    path("update_project/<project_id>/", views.update_project_view, name="update_project_view"),
    path("delete_project/<project_id>/", views.delete_project_view, name="delete_project_view"),
]