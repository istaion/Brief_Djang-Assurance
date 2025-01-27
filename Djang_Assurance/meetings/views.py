from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import StaffMetting
from .forms import StaffMeetingForm
from django.contrib.auth.mixins import LoginRequiredMixin

class MeetingListView(LoginRequiredMixin, ListView):
    model = StaffMetting
    template_name = 'meetings/meeting_list.html'
    
    def get_queryset(self):
        # Affiche les rendez-vous de l'utilisateur connecté
        return StaffMetting.objects.filter(requester=self.request.user)

class MeetingCreateView(LoginRequiredMixin, CreateView):
    model = StaffMetting
    form_class = StaffMeetingForm
    template_name = 'meetings/meeting_create.html'
    success_url = reverse_lazy('meeting_list')

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)