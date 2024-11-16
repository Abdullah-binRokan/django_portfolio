from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Project
from .forms import ProjectForm
from django.contrib import messages

# Create your views here.
def home_view(request: HttpRequest):
    projects = Project.objects.all()

    return render(request, "main/index.html", {"projects": projects})


def about_view(request: HttpRequest):

    return render(request, "main/about.html")


def contact_view(request: HttpRequest):

    return render(request, "main/contact.html")


def add_project_view(request: HttpRequest):
    # using django ModelForm
    if request.method == "POST":
        project_form = ProjectForm(request.POST, request.FILES)
        if project_form.is_valid():
            project_form.save()
            messages.success(request, "Project added successfuly!")
        else:
            messages.error(request, "There was an error. Please try again.")
    else:
        project_form = ProjectForm()

    return render(request, "main/add_project.html")


def update_project_view(request: HttpRequest, project_id: int):
    try:
        # get the post by the id
        project = Project.objects.get(pk = project_id)

        # Check if the form was submited by post method
        if request.method == "POST":
            project.name = request.POST["name"]
            project.description = request.POST["description"]
            # check if the images updatedd
            if "image" in request.FILES:
                project.image = request.FILES["image"]
            if "details_image" in request.FILES:
                project.details_image = request.FILES["details_image"]
            project.save()
            messages.success(request, "Project updated successfuly!")

    except:
        messages.error(request, "There was an error. Please try again.")

    return render(request, "main/update_project.html", {"project": project})


def delete_project_view(request: HttpRequest, project_id):
    try:
        project = Project.objects.get(pk = project_id)
        project.delete()

    except:
        return redirect("main:home_view")

    return render(request, "main/index.html")