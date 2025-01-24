from django.urls import path
from .views import InscriptionForm, Connexion, Accueil

urlpatterns = [
    path('', Accueil.as_view(), name='accueil'),
    path('inscription/', InscriptionForm, name='inscription'),
    path('connexion/', Connexion.as_view(), name='connexion'),
]
