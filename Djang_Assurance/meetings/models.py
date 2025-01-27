from django.db import models
from user.models import CustomUser, StaffUser
from datetime import datetime, timedelta
from django_agenda.models import AbstractBooking
from django_agenda.time_span import TimeSpan
from django_agenda.models import (AbstractAvailability,
                                  AbstractAvailabilityOccurrence,
                                  AbstractTimeSlot)

class Availability(AbstractAvailability):
    class AgendaMeta:
        schedule_model = StaffUser
        schedule_field = "staff"


class AvailabilityOccurrence(AbstractAvailabilityOccurrence):
    class AgendaMeta:
        availability_model = Availability
        schedule_model = StaffUser
        schedule_field = "staff"


class TimeSlot(AbstractTimeSlot):
    class AgendaMeta:
        availability_model = Availability
        schedule_model = StaffUser
        schedule_field = "staff"
        booking_model = "StaffMetting"


class StaffMetting(AbstractBooking):
    class AgendaMeta:
        schedule_model = StaffUser

    owner = models.ForeignKey(
        to=CustomUser,
        on_delete=models.PROTECT,
        related_name="meeting",
    )
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField(db_index=True)
    approved = models.BooleanField(default=False)
    subject = models.CharField(max_length=255, help_text="Sujet du rendez-vous")
    notes = models.TextField(blank=True, null=True, help_text="Notes pour le rendez-vous")

    def get_reserved_spans(self):
        # we only reserve the time if the reservation has been approved
        if self.approved:
            yield TimeSpan(self.start_time, self.end_time)


# class Meeting(models.Model):
#     """
#     Modèle de rendez-vous.
#     """
#     requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requester_meetings')
#     staff_member = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='staff_meetings', limit_choices_to={'is_staff': True})
#     date = models.DateTimeField()
#     duration = models.DurationField(default=timedelta(hours=1))
#     subject = models.CharField(max_length=255, help_text="Sujet du rendez-vous")
#     notes = models.TextField(blank=True, null=True, help_text="Notes pour le rendez-vous")

#     def __str__(self):
#         return f"{self.subject} ({self.requester.username} avec {self.staff_member.username})"

#     class Meta:
#         ordering = ['date']