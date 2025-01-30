from django.db import models

# Create your models here.


class ContactBase(models.Model):
    name = models.CharField(max_length=100, null=False)
    mail = models.CharField(max_length=250, null=False)
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True)