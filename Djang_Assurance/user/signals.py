from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, StaffUser

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