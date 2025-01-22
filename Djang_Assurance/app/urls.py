from django.urls import path
from .views import PredictionView, PredictionsListView, ResultView

urlpatterns = [
    path('prediction/', PredictionView.as_view(), name='prediction'),
    path('prediction/results/', PredictionsListView.as_view(), name='results'),
    path('prediction/result/<pk>', ResultView.as_view(), name='result'),
]