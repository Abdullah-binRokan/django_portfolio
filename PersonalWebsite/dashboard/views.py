from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from main.models import Project, ContactMessage
from blog.models import Post

# Create your views here.
def dashboard_projects_view(request: HttpRequest):
    projects = Project.objects.all()

    # sort based on order_by
    if "order_by" in request.GET:
        # get the value of "order_by"
        order_by = request.GET.get("order_by")
        if order_by == "name":
            projects = projects.order_by("name")
        elif order_by == "submitted_at":
            projects = projects.order_by("-submitted_at")

    # sort based on search
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        projects = projects.filter(name__contains = request.GET["search"])

    return render(request, "dashboard/projects.html", {"projects": projects})


def dashboard_messages_view(request: HttpRequest):
    messages = ContactMessage.objects.all()

    # sort based on order_by
    if "order_by" in request.GET:
        # get the value of "order_by"
        order_by = request.GET.get("order_by")
        if order_by == "name":
            messages = messages.order_by("name")
        elif order_by == "submitted_at":
            messages = messages.order_by("-submitted_at")

    # sort based on search
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        messages = messages.filter(name__contains = request.GET["search"])

    return render(request, "dashboard/messages.html", {"messages": messages})


def dashboard_posts_view(request: HttpRequest):
    posts = Post.objects.all()

    # sort based on order_by
    if "order_by" in request.GET:
        # get the value of "order_by"
        order_by = request.GET.get("order_by")
        if order_by == "name":
            posts = posts.order_by("name")
        elif order_by == "submitted_at":
            posts = posts.order_by("-submitted_at")

    # sort based on search
    if "search" in request.GET and len(request.GET["search"]) >= 1:
        posts = posts.filter(name__contains = request.GET["search"])

    return render(request, "dashboard/posts.html", {"posts": posts})
