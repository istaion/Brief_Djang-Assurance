from django.urls import path, include
from .views import StaffAgendaView, StaffUserListView, SelectDateView, SelectTimeslotView, UserListView

urlpatterns = [
    path('list/', StaffAgendaView.as_view(), name='meeting_list'),
    path('staff/', StaffUserListView.as_view(), name='staff_list'),
    path('user/', UserListView.as_view(), name= 'user_meeting_list'),
    path('staff/<int:staff_user_id>/select_date/', SelectDateView.as_view(), name='select_date'),
    path('staff/<int:staff_user_id>/select_timeslot/<str:date>/', SelectTimeslotView.as_view(), name='select_timeslot'),
]
    # path('appointment/<int:staff_user_id>/', AppointmentCreateView.as_view(), name='appointment_create'),