from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import ProjectForm
from django.contrib import messages

# Create your views here.
def home_view(request: HttpRequest):

    return render(request, "main/index.html")


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