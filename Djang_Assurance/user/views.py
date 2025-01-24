from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib import messages
from .forms import InscriptionForm
from django.contrib.auth.views import LoginView

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
            return redirect('inscription')  
    else:
        form = InscriptionForm()

    return render(request, 'user/inscription.html', {'form': form})

class Connexion(LoginView):
    success_url = reverse_lazy('Accueil')
    template_name = 'user/connexion.html'
    redirect_authenticated_user = True