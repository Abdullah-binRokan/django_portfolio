from django import forms
from .models import Project

# Create the form class 
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"