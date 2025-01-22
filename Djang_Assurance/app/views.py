from django.shortcuts import render, HttpResponseRedirect, redirect
import os
from django.views.generic import FormView, CreateView, ListView, DetailView
from .forms import PredictionForm
import pickle
import cloudpickle
import pandas as pd
import sklearn
from app.regression.regression_model import AgeTransformer, BmiTransformer
from .models import Prediction, Reg_model

class PredictionView(CreateView):
    model = Prediction
    template_name = 'app/prediction.html'
    form_class = PredictionForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.pred()
        self.object.save()
        prediction_id = self.object.id
        return redirect('result', pk=prediction_id)


class PredictionsListView(ListView):
    model = Prediction
    template_name = 'app/results.html'
    context_object_name = 'predictions'

class ResultView(DetailView):
    model = Prediction
    template_name = 'app/result.html'
    context_object_name = 'prediction'