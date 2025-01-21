from django.urls import path
from .views import PredictionView

urlpatterns = [
    path('prediction/', PredictionView.as_view(), name='prediction'),
]