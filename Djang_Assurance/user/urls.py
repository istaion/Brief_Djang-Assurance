from django.urls import path
from user import views
from .views import Connexion, debug_logout_view, acceuil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', Connexion.as_view(), name='connexion'),
    path('logout/',  debug_logout_view, name='logout' ),
    path('', acceuil, name='acceuil')
]

    # path('logout/',  LogoutView.as_view(next_page='/connexion/'), name='logout' )
