from django.shortcuts import render
from django.views.generic import FormView
from .forms import PredictionForm

class PredictionView(FormView):
    template_name = 'app/prediction.html'
    form_class = PredictionForm
