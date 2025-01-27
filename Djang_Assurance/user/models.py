from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    prenom = models.CharField(max_length=30, null= False)
    nom = models.CharField(max_length=30, null=False)
    age = models.PositiveIntegerField(null=True, blank= True)
    adresse= models.TextField(null=True, blank= True)