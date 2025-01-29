from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    prenom = models.CharField(max_length=30, null=False)
    nom = models.CharField(max_length=30, null=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

class StaffUser(models.Model):
    img = models.ImageField(upload_to='staff_users/', null=True, blank=True)
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE,  # Supprime le StaffUser si CustomUser est supprimé
        primary_key=True  # Utilise le même ID que CustomUser
    )

    class Meta:
        verbose_name = "Staff User"
        verbose_name_plural = "Staff Users"


