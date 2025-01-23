from django.urls import path
from .views import PredictionView, PredictionsListView, ResultView, UserPredictionView,UserResultView

urlpatterns = [
    path('unicorn/prediction/', PredictionView.as_view(), name='prediction'),
    path('unicorn/prediction/results/', PredictionsListView.as_view(), name='results'),
    path('unicorn/prediction/result/<pk>', ResultView.as_view(), name='result'),
    path('prediction/', UserPredictionView.as_view(), name='user_prediction'),
    path('prediction/result/<pk>', UserResultView.as_view(), name='user_result'),
]