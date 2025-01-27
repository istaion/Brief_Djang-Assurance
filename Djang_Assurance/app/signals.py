from django.db.models.signals import post_migrate
from django.dispatch import receiver
from user.models import CustomUser
from .models import Reg_model, Prediction


@receiver(post_migrate)
def after_migrations(sender, **kwargs):
    if not Reg_model.objects.all():
        # Créer les modèles
        Reg_model.objects.create(name = "linéaire basique", path="app/regression/models/basic_linreg_model.pkl")
        Reg_model.objects.create(name = "Gradient boosting", path="app/regression/models/gb_model.pkl")
        Reg_model.objects.create(name = "linéaire", path="app/regression/models/linreg_model.pkl")
        Reg_model.objects.create(name = "random forest", path="app/regression/models/rf_model.pkl")
        Reg_model.objects.create(name = "ridge_model", path="app/regression/models/ridge_model.pkl")
        Reg_model.objects.create(name = "lasso model", path="app/regression/models/best_lasso_model.pkl")

        # Créer des utilisateurs
        superuser = CustomUser.objects.create_user(username='superuser', prenom='super', nom='user', password='password', is_staff=True, is_superuser = True)
        user1 = CustomUser.objects.create_user(username='JeanMichou', prenom='Jean', nom='Michou', password='password')
        user2 = CustomUser.objects.create_user(username='gisèle', prenom='gis', nom='elle', password='password')
        user3 = CustomUser.objects.create_user(username='raouf', prenom='Ra', nom='Ouf', password='password', is_staff=True)
        user4 = CustomUser.objects.create_user(username='vic', prenom='vic', nom='tor', password='password', is_staff=True)
        user5 = CustomUser.objects.create_user(username='ludivine', prenom='Lu', nom='Divine', password='password', is_staff=True)

        # # Créer des prédictions pour chaque utilisateur
        # Prediction.objects.create(user_id=user1, made_by=user3, age=30, children=2, weight=70.5, size=170, smoker='no', region='southwest', result=200.0)
        # Prediction.objects.create(user_id=user2, made_by=user3, age=40, children=1, weight=80.2, size=175, smoker='yes', region='northeast', result=350.0)

        print('Données initialisées avec succes !')