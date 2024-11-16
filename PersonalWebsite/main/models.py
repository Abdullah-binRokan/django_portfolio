from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="project/images", default = "default.jpg")
    details_image = models.ImageField(upload_to="project/images", default = "default.jpg")