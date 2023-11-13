from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=2000)
