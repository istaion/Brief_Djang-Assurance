from django import forms
from .models import CustomUser

class InscriptionForm(forms.ModelForm):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    class Meta:
        model = CustomUser
        fields = ['email', 'prenom', 'nom', 'mot_de_passe', 'username','age', 'adresse'] 
        labels= {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse e-mail',
            'age': 'Age',
            'adresse': 'Adresse physique'
        }


class ModifProfilForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['prenom', 'nom', 'email', 'age', 'adresse']  # Liste des champs modifiables
