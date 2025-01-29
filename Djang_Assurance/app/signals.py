from django.db.models.signals import post_migrate
from django.dispatch import receiver
from user.models import CustomUser, StaffUser
from .models import Reg_model, Prediction


@receiver(post_migrate)
def after_migrations(sender, **kwargs):
    if not Reg_model.objects.all():
        # Créer les modèles
        print('Initialisation des modèles...')
        reg1 = Reg_model.objects.create(name = "linéaire basique", path="app/regression/models/basic_linreg_model.pkl")
        reg2 = Reg_model.objects.create(name = "Gradient boosting", path="app/regression/models/gb_model.pkl")
        reg3 = Reg_model.objects.create(name = "linéaire", path="app/regression/models/linreg_model.pkl")
        reg4 = Reg_model.objects.create(name = "random forest", path="app/regression/models/rf_model.pkl")
        reg5 = Reg_model.objects.create(name = "ridge_model", path="app/regression/models/ridge_model.pkl")
        reg6 = Reg_model.objects.create(name = "lasso model", path="app/regression/models/best_lasso_model.pkl")

        # Créer des utilisateurs
        print('Initialisation des utilisateurs...')
        superuser = CustomUser.objects.create_user(username='superuser', prenom='super', nom='user', password='password', is_superuser = True)
        user1 = CustomUser.objects.create_user(username='JeanMichou', prenom='Jean', nom='Michou', password='password')
        user2 = CustomUser.objects.create_user(username='gisèle', prenom='gis', nom='elle', password='password')
        user3 = CustomUser.objects.create_user(username='raouf', prenom='Ra', nom='Ouf', password='password', is_staff=True)
        user4 = CustomUser.objects.create_user(username='vic', prenom='vic', nom='tor', password='password', is_staff=True)
        user5 = CustomUser.objects.create_user(username='ludivine', prenom='Lu', nom='Divine', password='password', is_staff=True)
        print('Initialisation des staffusers...')
        # 💡 On s'assure que le signal post_save a bien créé les StaffUser
        staff1, _ = StaffUser.objects.get_or_create(user=user3)
        staff1.img = "staff_users/raouf_licorne.jpg"
        staff1.save()

        staff2, _ = StaffUser.objects.get_or_create(user=user4)
        staff2.img = "staff_users/vic_licorne.jpg"
        staff2.save()

        staff3, _ = StaffUser.objects.get_or_create(user=user5)
        staff3.img = "staff_users/ludi_licorne.jpg"
        staff3.save()

        # # Créer des prédictions pour chaque utilisateur
        print('Initialisation des prédictions...')
        pred_list = []
        pred_list.append(Prediction.objects.create(user_id=user1, made_by=user3, age=30, reg_model = reg1, children=2, weight=70.5, size=170, smoker='no', region='southwest'))
        pred_list.append(Prediction.objects.create(user_id=user2, made_by=user3, age=40, reg_model = reg2, children=1, weight=80.2, size=175, smoker='yes', region='northeast'))
        pred_list.append(Prediction.objects.create(user_id=user2, made_by=user4, age=50, reg_model = reg3, children=0, weight=90.2, size=165, smoker='yes', region='southeast'))
        pred_list.append(Prediction.objects.create(user_id=user1, made_by=user3, age=45, reg_model = reg4, children=4, weight=103, size=197, smoker='no', region='southwest'))
        pred_list.append(Prediction.objects.create(user_id=user2, made_by=user3, age=70, reg_model = reg5, children=3, weight=150, size=145, smoker='no', region='northeast'))
        pred_list.append(Prediction.objects.create(user_id=user1, made_by=user4, age=55, reg_model = reg6, children=5, weight=45, size=160, smoker='yes', region='southeast'))
        for pred in pred_list:
            pred.pred()  # Compute the prediction result.
            pred.fr_transform()  # Localize certain fields (e.g., sex, smoker).
            pred.save()
        
        print('Données initialisées avec succes !')