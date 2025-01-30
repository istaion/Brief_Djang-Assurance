from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, ListView, DetailView, FormView, View
from .forms import PredictionForm, UserPredictionForm, PredictionFilterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from user.permissions import StaffRequiredMixin, UserRequiredMixin
from .models import Prediction

# Team Unicorn: Views for handling Predictions

class PredictionView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
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
        self.object.made_by_staff = True
        self.object.pred()  # Compute the prediction result.
        self.object.fr_transform()  # Localize certain fields (e.g., sex, smoker).
        self.object.made_by = self.request.user
        self.object.save()  # Save the object to the database.
        prediction_id = self.object.id
        return redirect('result', pk=prediction_id)  # Redirect to the result page.

class PredictionUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Prediction
    template_name = 'app/prediction_update.html'
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
        self.object.made_by_staff = True
        self.object.pred()  # Compute the prediction result.
        self.object.fr_transform()  # Localize certain fields (e.g., sex, smoker).
        self.object.made_by = self.request.user
        self.object.save()  # Save the object to the database.
        prediction_id = self.object.id
        return redirect('result', pk=prediction_id)  # Redirect to the result page.
    
class PredictionDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Prediction
    template_name = 'app/prediction_confirm_delete.html'
    success_url = reverse_lazy('results')



class PredictionsListView(LoginRequiredMixin, StaffRequiredMixin, ListView, FormView):
    """
    Vue combinée ListView et FormView pour afficher les prédictions avec
    options de filtrage et de tri.
    """
    model = Prediction
    template_name = 'app/results.html'
    context_object_name = 'predictions'
    form_class = PredictionFilterForm

    def get_form(self, form_class=None):
        """
        Retourne une instance du formulaire lié avec les données de la requête.
        """
        if form_class is None:
            form_class = self.get_form_class()
        # Lie les données GET au formulaire
        return form_class(self.request.GET or None)

    def get_queryset(self):
        """
        Applique les filtres et les tris selon les données du formulaire.
        """
        print("get_queryset is called") 
        queryset = super().get_queryset()
        form = self.get_form()
        if form.is_valid():
            # Filtres
            user = form.cleaned_data.get('user')
            min_age = form.cleaned_data.get('min_age')
            max_age = form.cleaned_data.get('max_age')
            min_children = form.cleaned_data.get('min_children')
            max_children = form.cleaned_data.get('max_children')
            min_weight = form.cleaned_data.get('min_weight')
            max_weight = form.cleaned_data.get('max_weight')
            min_size = form.cleaned_data.get('min_size')
            max_size = form.cleaned_data.get('max_size')
            sex = form.cleaned_data.get('sex')
            smoker = form.cleaned_data.get('smoker')
            region = form.cleaned_data.get('region')
            reg_model = form.cleaned_data.get('reg_model')

            if user:
                queryset = queryset.filter(user_id__username__icontains=user)
            if min_age is not None:
                queryset = queryset.filter(age__gte=min_age)
            if max_age is not None:
                queryset = queryset.filter(age__lte=max_age)
            if min_children is not None:
                queryset = queryset.filter(children__gte=min_children)
            if max_children is not None:
                queryset = queryset.filter(children__lte=max_children)
            if min_weight is not None:
                queryset = queryset.filter(weight__gte=min_weight)
            if max_weight is not None:
                queryset = queryset.filter(weight__lte=max_weight)
            if min_size is not None:
                queryset = queryset.filter(size__gte=min_size)
            if max_size is not None:
                queryset = queryset.filter(size__lte=max_size)
            if sex:
                queryset = queryset.filter(sex=sex)
            if smoker:
                queryset = queryset.filter(smoker=smoker)
            if region:
                queryset = queryset.filter(region=region)
            if reg_model:
                queryset = queryset.filter(reg_model_id__name__icontains=reg_model)

            # Tri
            sort_by = form.cleaned_data.get('sort_by')
            order = form.cleaned_data.get('order', 'asc')
            if sort_by:
                if order == "desc":
                    sort_by = f"-{sort_by}"  # Tri descendant
                queryset = queryset.order_by(sort_by)
        else:
            print("Form is not valid:", form.errors)
        return queryset



class ResultView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    """
    Displays the details of a single Prediction object.
    """
    model = Prediction
    template_name = 'app/result.html'
    context_object_name = 'prediction'  # Use 'prediction' as the context variable in the template.


# Views for User-specific Predictions


class UserPredictionView(LoginRequiredMixin, UserRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            # Vérifie si une prédiction existe pour l'utilisateur
            prediction = Prediction.objects.get(made_by = request.user)
            return redirect('user_result', pk=prediction.id)
        except Prediction.DoesNotExist:
            # Sinon, redirige vers 'user_create'
            return redirect('user_create')

class UserCreatePredictionView(LoginRequiredMixin, UserRequiredMixin, CreateView):
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
        self.object.user_id = self.request.user
        self.object.made_by = self.request.user
        self.object.save()  # Save the object to the database.
        prediction_id = self.object.id
        return redirect('user_result', pk=prediction_id)  # Redirect to the user-specific result page.


class UserResultView(LoginRequiredMixin, UserRequiredMixin, DetailView):
    """
    Displays the details of a single Prediction object created by a user.
    """
    model = Prediction
    template_name = 'app/user_result.html'
    context_object_name = 'prediction'  # Use 'prediction' as the context variable in the template.

class UserPredictionUpdateView(LoginRequiredMixin, UserRequiredMixin, UpdateView):
    model = Prediction
    template_name = 'app/user_prediction_update.html'
    form_class = UserPredictionForm

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
        self.object.made_by = self.request.user
        self.object.user_id = self.request.user
        self.object.save()  # Save the object to the database.
        prediction_id = self.object.id
        return redirect('user_result', pk=prediction_id)  # Redirect to the result page.