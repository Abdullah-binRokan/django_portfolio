from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_view, name="blog_view"),
    path("add_post/", views.add_post_view, name="add_post_view"),
    path("update_post/<post_id>/", views.update_post_view, name="update_post_view"),
    path("delete_post/<post_id>/", views.delete_post_view, name="delete_post_view"),
]