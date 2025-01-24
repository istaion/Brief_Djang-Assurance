from django.db import models
from ..user.models import CustomUser
from django_agenda.models import (AbstractAvailability,
                                  AbstractAvailabilityOccurrence,
                                  AbstractTimeSlot)
from django_agenda.models import AbstractBooking
from django_agenda.time_span import TimeSpan

# class Availability(AbstractAvailability):
#     class AgendaMeta:
#         schedule_model = User
#         schedule_field = "utilisateur"  # optional


# class AvailabilityOccurrence(AbstractAvailabilityOccurrence):
#     class AgendaMeta:
#         availability_model = Availability
#         schedule_model = User
#         schedule_field = "utilisateur"  # optional


# class TimeSlot(AbstractTimeSlot):
#     class AgendaMeta:
#         availability_model = Availability
#         schedule_model = User
#         booking_model = "RoomReservation" # booking class, more details shortly
#         schedule_field = "utilisateur"  # optional

# class MeetingReservation(AbstractBooking):
#     class AgendaMeta:
#         schedule_model = User

#     owner = models.ForeignKey(
#         to=settings.AUTH_USER_MODEL,
#         on_delete=models.PROTECT,
#         related_name="reservations",
#     )
#     start_time = models.DateTimeField(db_index=True)
#     end_time = models.DateTimeField(db_index=True)
#     approved = models.BooleanField(default=False)

#     def get_reserved_spans(self):
#         # we only reserve the time if the reservation has been approved
#         if self.approved:
#             yield TimeSpan(self.start_time, self.end_time)