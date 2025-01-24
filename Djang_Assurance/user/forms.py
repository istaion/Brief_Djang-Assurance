from django import forms
from .models import CustomUser

class InscriptionForm(forms.ModelForm):
    prenom = forms.CharField(max_length=30, required=True, label="Prénom")
    nom = forms.CharField(max_length=30, required=True, label="Nom")
    mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    confirmation_mot_de_passe = forms.CharField(widget=forms.PasswordInput, label="Confirmez le mot de passe")

    class Meta:
        model = CustomUser
        fields = ['username', 'prenom', 'nom', 'email']

    def clean(self):
        cleaned_data = super().clean()
        mot_de_passe = cleaned_data.get("mot_de_passe")
        confirmation_mot_de_passe = cleaned_data.get("confirmation_mot_de_passe")

        if mot_de_passe != confirmation_mot_de_passe:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
