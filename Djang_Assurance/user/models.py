from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    prenom = models.CharField(max_length=30, null=False)
    nom = models.CharField(max_length=30, null=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

class StaffUser(models.Model):
    img = models.FilePathField(path='app/regression/models/', null=True)
    user = models.OneToOneField(
        CustomUser, 
        on_delete=models.CASCADE,  # Supprime le StaffUser si CustomUser est supprimé
        primary_key=True  # Utilise le même ID que CustomUser
    )

    class Meta:
        verbose_name = "Staff User"
        verbose_name_plural = "Staff Users"


# Signal post-save pour créer automatiquement un StaffUser
@receiver(post_save, sender=CustomUser)
def create_staff_user(sender, instance, created, **kwargs):
    if instance.is_staff:
        # Vérifie si un StaffUser correspondant existe déjà
        StaffUser.objects.get_or_create(
            user=instance,  # Utilise le champ OneToOneField pour la liaison
            defaults={
                # Les champs supplémentaires peuvent être initialisés ici
            },
        )
