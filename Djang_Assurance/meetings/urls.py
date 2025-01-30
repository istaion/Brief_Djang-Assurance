from django.urls import path, include
from .views import StaffAgendaView, StaffUserListView, SelectDateView, SelectTimeslotView, UserListView

urlpatterns = [
    path('staff/', StaffUserListView.as_view(), name='staff_list'),
    path('user/', UserListView.as_view(), name= 'user_meeting_list'),
    path('staff/<int:staff_user_id>/select_date/', SelectDateView.as_view(), name='select_date'),
    path('staff/<int:staff_user_id>/select_timeslot/<str:date>/', SelectTimeslotView.as_view(), name='select_timeslot'),
    path('agenda/', StaffAgendaView.as_view(), name='agenda'),
    path('agenda/<str:week_start_date>/', StaffAgendaView.as_view(), name='agenda_by_date'),
]
    # path('appointment/<int:staff_user_id>/', AppointmentCreateView.as_view(), name='appointment_create'),