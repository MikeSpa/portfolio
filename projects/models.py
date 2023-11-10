from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=63)
    description = models.TextField(max_length=1000)
    url = models.URLField(max_length=200)
    image = models.FileField(upload_to="projects_images/", blank=True)

    def __str__(self):
        return self.title
