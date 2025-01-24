from django import forms
from .models import CustomUser

class InscriptionForm(forms.ModelForm):
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")

    class Meta:
        model = CustomUser
        fields = ['email', 'prenom', 'nom', 'mot_de_passe'] 
