from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="projects/images", default = "default.jpg")
    details_image = models.ImageField(upload_to="projects/images", default = "default.jpg")


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()