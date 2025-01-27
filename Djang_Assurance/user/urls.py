from django.urls import path
from .views import InscriptionView, Connexion, DeconnexionView, Accueil, ProfilView, ModifProfilView, acceuil

urlpatterns = [
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('connexion/', Connexion.as_view(), name='connexion'),
    path('deconnexion/', DeconnexionView.as_view(), name='deconnexion'),
    path('accueil/', Accueil.as_view(), name='accueil'),
    path('accueil2/', acceuil, name='accueil2'),
    path('profil/', ProfilView.as_view(), name='profil'),
    path('modifier-profil/', ModifProfilView.as_view(), name='modification'),
]

