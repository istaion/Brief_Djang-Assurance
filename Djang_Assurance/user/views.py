from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from models import InscriptionForm

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
            return redirect('connexion')  # Remplacez par l'URL de la vue de connexion
    else:
        form = InscriptionForm()

    return render(request, 'utilisateurs/inscription.html', {'form': form})
