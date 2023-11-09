from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=40)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
