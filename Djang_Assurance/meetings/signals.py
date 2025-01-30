from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import StaffUser
from .models import Availability
from datetime import time, datetime

@receiver(post_save, sender=StaffUser)
def create_default_availability(sender, instance, created, **kwargs):
    if created:  # Nous ne créons les disponibilités que si le StaffUser vient d'être créé
        for day in range(5):  # Lundi à Vendredi
            # Vérifier si la disponibilité existe déjà pour ce StaffUser et ce jour de la semaine
            if not Availability.objects.filter(
                staff_user=instance,
                day_of_week=day,
                start_time=time(13, 0),  # 13:00
                end_time=time(16, 0)     # 16:00
            ).exists():
                # Créer la disponibilité uniquement si elle n'existe pas déjà
                Availability.objects.create(
                    staff_user=instance,
                    day_of_week=day,
                    start_time=time(13, 0),  # 13:00
                    end_time=time(16, 0)     # 16:00
                )