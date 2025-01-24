from django.urls import path
from user import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
]
