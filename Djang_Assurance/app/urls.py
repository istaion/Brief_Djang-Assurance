from django.urls import path
from .views import (
    PredictionView,
    PredictionsListView,
    ResultView,
    UserPredictionView,
    UserResultView,
    PredictionDeleteView,
    PredictionUpdateView,
    UserCreatePredictionView,
    UserPredictionUpdateView
)

urlpatterns = [
    # Routes pour les prédictions générales
    path('unicorn/prediction/', PredictionView.as_view(), name='prediction'),
    path('unicorn/prediction/results/', PredictionsListView.as_view(), name='results'),
    path('unicorn/prediction/result/<int:pk>/', ResultView.as_view(), name='result'),
    path('unicorn/prediction/result/update/<int:pk>/', PredictionUpdateView.as_view(), name='prediction_update'),
    path('unicorn/prediction/result/delete/<int:pk>/', PredictionDeleteView.as_view(), name='prediction_delete'),

    # Routes pour les prédictions liées à l'utilisateur
    path('prediction/', UserPredictionView.as_view(), name='user_prediction'),
    path('prediction/create/', UserCreatePredictionView.as_view(), name='user_create'),
    path('prediction/result/<int:pk>/', UserResultView.as_view(), name='user_result'),
    path('prediction/result/update/<int:pk>/', UserPredictionUpdateView.as_view(), name='user_update'),
]
