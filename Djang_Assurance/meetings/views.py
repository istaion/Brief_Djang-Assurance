from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import TemplateView, ListView
from .models import Availability, Appointment
from datetime import datetime, timedelta
from django.views import View
from user.models import StaffUser
from django.core.exceptions import ValidationError
from django.views.generic import TemplateView
from django.utils.timezone import localdate
from .models import Availability, Appointment, StaffUser
from django.contrib.auth.mixins import LoginRequiredMixin
from user.permissions import StaffRequiredMixin


class StaffAgendaView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'meetings/meetings_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupérer l'utilisateur authentifié
        staff_user = StaffUser.objects.get(user=self.request.user)
        
        # Récupérer la date de début de la semaine
        week_start_date = kwargs.get('week_start_date')
        
        if not week_start_date:
            # Si pas de date dans l'URL, on prend la date de la semaine en cours
            week_start_date = timezone.now().date() - timedelta(days=timezone.now().weekday())
        else:
            # Convertir la date de début de semaine en objet date
            week_start_date = timezone.datetime.strptime(week_start_date, '%Y-%m-%d').date()

        # Calculer la fin de la semaine
        week_end_date = week_start_date + timedelta(days=6)

        # Récupérer les disponibilités du StaffUser pour la semaine
        availabilities = Availability.objects.filter(staff_user=staff_user)

        # Récupérer les rendez-vous déjà pris pour le StaffUser sur la semaine
        appointments = Appointment.objects.filter(staff_user=staff_user, date__range=[week_start_date, week_end_date])

        # Préparer le contexte pour le template
        week_days = [0, 1, 2, 3, 4, 5, 6]  # Lundi à Dimanche
        time_slots = [f"{hour}:00" for hour in range(9, 19)]  # Créneaux de 9h à 18h

        # Initialiser une liste pour l'agenda
        agenda = []

        # Remplir l'agenda avec les disponibilités
        for day in week_days:
            for slot in time_slots:
                # Initialiser l'état à "Disponible"
                state = ""
                
                # Vérifier si ce créneau correspond à une disponibilité
                availability = availabilities.filter(
                    day_of_week=day,
                    start_time__lte=slot,
                    end_time__gte=slot,
                ).first()
                if availability:
                    state = "Disponible"
                
                # Vérifier si un rendez-vous a été pris
                appointment = appointments.filter(
                    date__week_day=day + 1,  # Django utilise 1 pour Lundi, 7 pour Dimanche
                    start_time=slot,
                ).first()
                if appointment:
                    print(appointment)
                    state = appointment.user.username  # Afficher le username du client

                agenda.append({
                    'day': day,
                    'slot': slot,
                    'state': state
                })

        # Ajouter les variables au contexte
        context['agenda'] = agenda
        context['days_of_week'] = Availability.DAYS_OF_WEEK
        context['time_slots'] = time_slots
        context['week_start_date'] = week_start_date
        context['previous_week'] = week_start_date - timedelta(days=7)
        context['next_week'] = week_start_date + timedelta(days=7)
        return context


class StaffUserListView(LoginRequiredMixin, ListView):
    model = StaffUser
    template_name = 'meetings/staff_user_list.html'
    context_object_name = 'staff_users'
    # def get(self, request):
    #     # Affiche tous les StaffUsers
    #     staff_users = StaffUser.objects.all()
    #     return render(request, 'meetings/staff_user_list.html', {'staff_users': staff_users})

class SelectDateView(LoginRequiredMixin, View):
    def get(self, request, staff_user_id):
        staff_user = get_object_or_404(StaffUser, user__id=staff_user_id)
        return render(request, 'meetings/select_date.html', {
            'staff_user': staff_user
        })

    def post(self, request, staff_user_id):
        staff_user = get_object_or_404(StaffUser, user__id=staff_user_id)
        selected_date = request.POST.get('date')

        # Vérifier si la date est bien sélectionnée
        if not selected_date:
            return render(request, 'meetings/select_date.html', {
                'staff_user': staff_user,
                'error': "Veuillez sélectionner une date."
            })

        # Rediriger vers la vue pour choisir l'heure
        return redirect('select_timeslot', staff_user_id=staff_user_id, date=selected_date)

class SelectTimeslotView(LoginRequiredMixin, View):
    def get(self, request, staff_user_id, date):
        staff_user = get_object_or_404(StaffUser, user__id=staff_user_id)
        selected_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Récupérer toutes les disponibilités du StaffUser pour cette date
        availabilities = Availability.objects.filter(staff_user=staff_user)

        # Créer une liste de créneaux horaires disponibles pour cette date
        available_timeslots = []
        for availability in availabilities:
            start_time = availability.start_time
            end_time = availability.end_time

            # Ajouter tous les créneaux horaires disponibles entre start_time et end_time pour la date sélectionnée
            current_time = start_time
            while current_time < end_time:
                available_timeslots.append(current_time)
                current_time = (datetime.combine(datetime.today(), current_time) + timedelta(hours=1)).time()

        # Vérifier les rendez-vous existants pour cette date spécifique et exclure les créneaux réservés
        booked_timeslots = Appointment.objects.filter(
            staff_user=staff_user,
            date=selected_date  # Filtrer par la date spécifiée
        ).values_list('start_time', flat=True)

        # Exclure les créneaux déjà réservés
        available_timeslots_duplicate = [slot for slot in available_timeslots if slot not in booked_timeslots]
        available_timeslots = list(set(available_timeslots_duplicate))
        print(available_timeslots)

        return render(request, 'meetings/select_timeslot.html', {
            'staff_user': staff_user,
            'available_timeslots': available_timeslots,
            'selected_date': selected_date.strftime('%Y-%m-%d')
        })

    def post(self, request, staff_user_id, date):
        staff_user = get_object_or_404(StaffUser, user__id=staff_user_id)
        start_time_str = request.POST.get('start_time')

        # Convertir le start_time (string) en objet time
        start_time = datetime.strptime(start_time_str, "%H:%M").time()

        # Convertir la date (string) en objet date
        selected_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Vérifier si le créneau est déjà réservé
        if Appointment.objects.filter(staff_user=staff_user, date=selected_date, start_time=start_time).exists():
            return render(request, 'meetings/select_timeslot.html', {
                'staff_user': staff_user,
                'error': "Ce créneau est déjà réservé.",
                'available_timeslots': available_timeslots,
                'selected_date': date
            })

        # Calculer l'end_time (1 heure après le start_time)
        end_time = (datetime.combine(datetime.today(), start_time) + timedelta(hours=1)).time()

        # Créer le rendez-vous
        Appointment.objects.create(
            user=request.user,
            staff_user=staff_user,
            date=selected_date,
            start_time=start_time,
            end_time=end_time  # Calculer la fin
        )

        return redirect('user_meeting_list')  # Redirection vers la liste des rendez-vous


class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'meetings/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer tous les rendez-vous de l'utilisateur connecté
        user_appointments = Appointment.objects.filter(user=self.request.user)

        # Ajouter ces rendez-vous au contexte
        context['user_appointments'] = user_appointments

        # Ajouter un lien vers la liste des StaffUser pour prendre un rendez-vous
        context['staff_list_url'] = 'staff_list'

        return context

