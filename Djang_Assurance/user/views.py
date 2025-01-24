from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from .forms import InscriptionForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout

def acceuil(request):
    if request.user.is_staff:
        return redirect('prediction')
    else:
        return redirect('user_prediction')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            utilisateur = form.save(commit=False)
            utilisateur.first_name = form.cleaned_data['prenom']
            utilisateur.last_name = form.cleaned_data['nom']
            utilisateur.set_password(form.cleaned_data['mot_de_passe'])
            utilisateur.save()
            messages.success(request, "Inscription réussie ! Vous pouvez maintenant vous connecter.")
            return redirect('connexion')  
    else:
        form = InscriptionForm()

    return render(request, 'user/inscription.html', {'form': form})

class Connexion(LoginView):
    template_name = 'user/connexion.html'

def debug_logout_view(request):
    logout(request)
    return redirect('connexion')  # Redirige vers la route nommée 'connexion'