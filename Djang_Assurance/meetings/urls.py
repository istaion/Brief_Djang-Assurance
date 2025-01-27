from django.urls import path
from .views import MeetingListView, MeetingCreateView

urlpatterns = [
    path('list/', MeetingListView.as_view(), name='meeting_list'),
    path('create/', MeetingCreateView.as_view(), name='meeting_create'),
]