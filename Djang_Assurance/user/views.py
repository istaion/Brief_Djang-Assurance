from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InscriptionForm, ModifProfilForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .permissions import StaffRequiredMixin
from .models import CustomUser

class AccueilView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff: 
            return redirect('prediction')
        else:
            return redirect('user_prediction')


class InscriptionView(FormView):
    template_name= 'user/inscription.html'
    form_class = InscriptionForm
    success_url = reverse_lazy('connexion')

    def form_valid(self, form):
        #sauvegarde du user
        utilisateur= form.save(commit=False)
        utilisateur.first_name = form.cleaned_data['prenom']
        utilisateur.last_name = form.cleaned_data['nom']
        utilisateur.set_password(form.cleaned_data['mot_de_passe'])
        utilisateur.save()

        #succes
        messages.success(self.request, 'Inscription réussie ! Vous pouvez maintenant vous connecter.')
        return super().form_valid(form)

    def form_invalid(self, form):
        #erreur
        messages.error(self.request, "Veuillez corriger les erreurs du formulaire.")
        return super().form_invalid(form)


class Connexion(LoginView):
    template_name = 'user/connexion.html'
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Nom d'utilisateur ou mot de passe incorrect. Veuillez réessayer.")
        return super().form_invalid(form)


class DeconnexionView(LogoutView):
    
    next_page = reverse_lazy('accueil')  


class Accueil(TemplateView):
    template_name= 'user/accueil.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
        

class ProfilView(LoginRequiredMixin,TemplateView):
    template_name = 'user/profil.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    

class ModifProfilView(LoginRequiredMixin, UpdateView):
    
    model = CustomUser
    form_class = ModifProfilForm
    template_name = 'user/modif_profil.html'
    success_url = reverse_lazy('accueil')

    def get_object(self):
        return self.request.user


class SuppressionUser(LoginRequiredMixin,View):
    template_name = 'user/suppression_compte.html'

    def get(self, request, *args, **kwargs):
        #afficher la page de confirmation
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        messages.success(request, "Votre compte a été supprimé avec succès.")
        return redirect('accueil')