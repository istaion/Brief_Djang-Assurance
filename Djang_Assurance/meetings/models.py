from django.db import models
from user.models import StaffUser, CustomUser


class Availability(models.Model):
    DAYS_OF_WEEK = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]

    staff_user = models.ForeignKey(StaffUser, on_delete=models.CASCADE, related_name='availabilities')
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)  # Ex : 0 = Monday
    start_time = models.TimeField()  # Ex : 13:00
    end_time = models.TimeField()    # Ex : 16:00

    class Meta:
        unique_together = ('staff_user', 'day_of_week', 'start_time', 'end_time')

    def __str__(self):
        return f"{self.get_day_of_week_display()} {self.start_time} - {self.end_time}"

class Appointment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments')  # Utilisateur qui prend le RDV
    staff_user = models.ForeignKey(StaffUser, on_delete=models.CASCADE, related_name='appointments_with_staff')  # StaffUser concerné
    date = models.DateField()  # Date du rendez-vous
    start_time = models.TimeField()  # Heure de début
    end_time = models.TimeField()    # Heure de fin

    class Meta:
        unique_together = ('staff_user', 'date', 'start_time', 'end_time')

    def __str__(self):
        return f"Appointment with {self.staff_user.user} on {self.date} from {self.start_time} to {self.end_time}"

    def clean(self):
        """
        Vérifie si le rendez-vous respecte les disponibilités du StaffUser.
        """
        from django.core.exceptions import ValidationError
        availability = Availability.objects.filter(
            staff_user=self.staff_user,
            day_of_week=self.date.weekday(),
            start_time__lte=self.start_time,
            end_time__gte=self.end_time,
        )
        if not availability.exists():
            raise ValidationError("This appointment is outside the staff user's availability.")


