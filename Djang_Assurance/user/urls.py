from django.urls import path
from .views import (
    InscriptionView,
    Connexion,
    DeconnexionView,
    Accueil,
    ProfilView,
    ModifProfilView,
    AccueilView,
    SuppressionUser,
)

urlpatterns = [
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('connexion/', Connexion.as_view(), name='connexion'),
    path('deconnexion/', DeconnexionView.as_view(), name='deconnexion'),
    path('accueil/', Accueil.as_view(), name='accueil'),
    path('profil/', ProfilView.as_view(), name='profil'),
    path('profil/modification/', ModifProfilView.as_view(), name='modification'),
    path('accueil/', AccueilView.as_view(), name='accueil_redirection'),
    path('suppression-compte', SuppressionUser.as_view(), name='suppression_compte'),


]

