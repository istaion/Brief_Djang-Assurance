from django.urls import path
from user import views
from .views import Connexion

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', Connexion.as_view(), name='connexion')
]
