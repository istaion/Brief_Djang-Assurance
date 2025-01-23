from django.shortcuts import render, HttpResponseRedirect, redirect
import os
from django.views.generic import FormView, CreateView, ListView, DetailView
from .forms import PredictionForm, UserPredictionForm
import pickle
import cloudpickle
import pandas as pd
import sklearn
from app.regression.regression_model import AgeTransformer, BmiTransformer
from .models import Prediction, Reg_model

# Team Unicorn: Views for handling Predictions

class PredictionView(CreateView):
    """
    Handles the creation of a new Prediction object.
    Uses the PredictionForm and redirects to the result page after saving.
    """
    model = Prediction
    template_name = 'app/prediction.html'
    form_class = PredictionForm

    def form_valid(self, form):
        """
        Process the form after validation:
        - Save the prediction object without committing to the database.
        - Call the `pred` method to compute the result.
        - Call `fr_transform` to localize the fields.
        - Save the object and redirect to the result view.
        """
        self.object = form.save(commit=False)  # Save the object without committing.
        self.object.pred()  # Compute the prediction result.
        self.object.fr_transform()  # Localize certain fields (e.g., sex, smoker).
        self.object.save()  # Save the object to the database.
        prediction_id = self.object.id
        return redirect('result', pk=prediction_id)  # Redirect to the result page.


class PredictionsListView(ListView):
    """
    Displays a list of all saved Prediction objects.
    """
    model = Prediction
    template_name = 'app/results.html'
    context_object_name = 'predictions'  # Use 'predictions' as the context variable in the template.


class ResultView(DetailView):
    """
    Displays the details of a single Prediction object.
    """
    model = Prediction
    template_name = 'app/result.html'
    context_object_name = 'prediction'  # Use 'prediction' as the context variable in the template.


# Views for User-specific Predictions

class UserPredictionView(CreateView):
    """
    Handles the creation of a new Prediction object for a user.
    Uses the UserPredictionForm and excludes fields like `reg_model` and `result`.
    Redirects to the user result page after saving.
    """
    model = Prediction
    template_name = 'app/user_prediction.html'
    form_class = UserPredictionForm

    def form_valid(self, form):
        """
        Process the form after validation:
        - Save the prediction object without committing to the database.
        - Compute the prediction result and localize certain fields.
        - Save the object and redirect to the user-specific result view.
        """
        self.object = form.save(commit=False)  # Save the object without committing.
        self.object.pred()  # Compute the prediction result.
        self.object.fr_transform()  # Localize certain fields (e.g., sex, smoker).
        self.object.save()  # Save the object to the database.
        prediction_id = self.object.id
        return redirect('user_result', pk=prediction_id)  # Redirect to the user-specific result page.


class UserResultView(DetailView):
    """
    Displays the details of a single Prediction object created by a user.
    """
    model = Prediction
    template_name = 'app/user_result.html'
    context_object_name = 'prediction'  # Use 'prediction' as the context variable in the template.