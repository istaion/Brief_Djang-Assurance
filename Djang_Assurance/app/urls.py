from django.urls import path
from .views import (PredictionView,
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
    path('unicorn/prediction/', PredictionView.as_view(), name='prediction'),
    path('unicorn/prediction/results/', PredictionsListView.as_view(), name='results'),
    path('unicorn/prediction/result/<pk>', ResultView.as_view(), name='result'),
    path('unicorn/prediction/result/update/<pk>', PredictionUpdateView.as_view(), name='prediction_update'),
    path('unicorn/prediction/result/delete/<pk>', PredictionDeleteView.as_view(), name='prediction_delete'),
    path('prediction/', UserPredictionView.as_view(), name='user_prediction'),
    path('prediction/create', UserCreatePredictionView.as_view(), name='user_create'),
    path('prediction/result/<pk>', UserResultView.as_view(), name='user_result'),
    path('prediction/result/update/<pk>', UserPredictionUpdateView.as_view(), name='user_update'),
]