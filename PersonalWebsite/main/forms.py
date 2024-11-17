from django import forms
from .models import Project, ContactMessage

# Create the form class 
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"