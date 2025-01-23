from django import forms
from .models import User, Reg_model, Prediction

class PredictionForm(forms.ModelForm):
    """
    Form for staff to create a Prediction object.

    Excludes the 'result' field because it is calculated dynamically and 
    should not be set manually by the user.
    """
    class Meta:
        model = Prediction
        fields = '__all__'
        exclude = ['result','made_by_staff']



class UserPredictionForm(forms.ModelForm):
    """
    Form for users to create a Prediction object.

    Excludes:
    - 'result': This is calculated dynamically.
    - 'reg_model': The regression model is null by default for choose the most 
    expensive prediction among all models..
    """
    class Meta:
        model = Prediction
        fields = '__all__'
        exclude = ['result', 'made_by_staff', 'reg_model']

def get_reg_model():
    list_reg_models = []
    reg_models = Reg_model.objects.all()
    for model in reg_models:
        list_reg_models.append((model.name,model.name))
    return list_reg_models

class PredictionFilterForm(forms.Form):
    """
    Formulaire pour rechercher et filtrer les prédictions.
    """
    user = forms.CharField(required=False, label="Nom d'utilisateur")
    min_age = forms.IntegerField(required=False, min_value=0, max_value=200, label="Âge minimum")
    max_age = forms.IntegerField(required=False, min_value=0, max_value=200, label="Âge maximum")
    min_children = forms.IntegerField(required=False, min_value=0, max_value=20, label="Nombre minimum d'enfants")
    max_children = forms.IntegerField(required=False, min_value=0, max_value=20, label="Nombre maximum d'enfants")
    min_weight = forms.FloatField(required=False, min_value=0, max_value=300, label="Poids minimum (kg)")
    max_weight = forms.FloatField(required=False, min_value=0, max_value=300, label="Poids maximum (kg)")
    min_size = forms.FloatField(required=False, min_value=0, max_value=300, label="Taille minimum (cm)")
    max_size = forms.FloatField(required=False, min_value=0, max_value=300, label="Taille maximum (cm)")
    sex = forms.ChoiceField(required=False, 
                            choices=[("", "Tous"),('femme', 'femme'),('homme','homme')], 
                            label="Genre")
    smoker = forms.ChoiceField(required=False, 
                               choices=[("", "Tous"),('oui','oui'),('non','non')], 
                               label="Fumeur")
    region = forms.ChoiceField(required=False, 
                               choices=[("", "Toutes"), ("Sud Est","Sud Est"), ("Sud Ouest","Sud Ouest"),
                                        ("Nord Ouest","Nord Ouest"), ("Nord Est","Nord Est") ], 
                               label="Région")
    reg_model = forms.ChoiceField(required=False, 
                               choices=get_reg_model(),
                               label="model")
    sort_by = forms.ChoiceField(
        required=False,
        choices=[
            ("age", "Âge"),
            ("weight", "Poids"),
            ("size", "Taille"),
            ("result", "Résultat"),
        ],
        label="Trier par",
    )
    order = forms.ChoiceField(
        required=False,
        choices=[("asc", "Ascendant"), ("desc", "Descendant")],
        label="Ordre",
    )



