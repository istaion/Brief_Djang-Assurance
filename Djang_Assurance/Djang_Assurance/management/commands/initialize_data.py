from django.core.management.base import BaseCommand
from user.models import CustomUser
from app.models import Prediction, Reg_model

class Command(BaseCommand):
    help = 'Initialise la base de données avec des utilisateurs et des prédictions'

    def handle(self, *args, **kwargs):
        # Créer les modèles
        Reg_model.objects.create(name = "", path="/basic_linreg_model.pkl")

        # Créer des utilisateurs
        user1 = CustomUser.objects.create_user(username='JeanMichou', prenom='Jean', nom='Michou', password='password')
        user2 = CustomUser.objects.create_user(username='gisèle', prenom='gis', nom='elle', password='password')
        user3 = CustomUser.objects.create_user(username='raouf', prenom='Ra', nom='Ouf', password='password', is_staff=True)
        user4 = CustomUser.objects.create_user(username='vic', prenom='vic', nom='tor', password='password', is_staff=True)
        user5 = CustomUser.objects.create_user(username='ludivine', prenom='Lu', nom='Divine', password='password', is_staff=True)

        # Créer des prédictions pour chaque utilisateur
        Prediction.objects.create(user_id=user1, made_by=user3, age=30, children=2, weight=70.5, size=170, smoker='no', region='southwest', result=200.0)
        Prediction.objects.create(user_id=user2, made_by=user3, age=40, children=1, weight=80.2, size=175, smoker='yes', region='northeast', result=350.0)

        self.stdout.write(self.style.SUCCESS('Données initialisées avec succes !'))