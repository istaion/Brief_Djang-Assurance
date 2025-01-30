from django import forms
from .models import Reg_model, Prediction
from django.db.utils import OperationalError

class PredictionForm(forms.ModelForm):
    """
    Form for staff to create a Prediction object.

    Excludes the 'result' field because it is calculated dynamically and 
    should not be set manually by the user.
    """
    class Meta:
        model = Prediction
        fields = '__all__'
        exclude = ['result','made_by_staff', 'made_by']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["sex"] in {'homme', 'femme'}:
            prediction = Prediction(**cleaned_data)  # Création temporaire d'une instance
            prediction.en_transform()  # Appliquer la transformation en anglais
            
            # Mettre à jour les valeurs dans cleaned_data
            cleaned_data["sex"] = prediction.sex
            cleaned_data["smoker"] = prediction.smoker
            cleaned_data["region"] = prediction.region
            return cleaned_data
        else:
            return cleaned_data

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
        exclude = ['result', 'made_by_staff', 'reg_model', 'user_id', 'made_by']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["sex"] in {'homme', 'femme'}:
            prediction = Prediction(**cleaned_data)  # Création temporaire d'une instance
            prediction.en_transform()  # Appliquer la transformation en anglais
            
            # Mettre à jour les valeurs dans cleaned_data
            cleaned_data["sex"] = prediction.sex
            cleaned_data["smoker"] = prediction.smoker
            cleaned_data["region"] = prediction.region
            return cleaned_data
        else:
            return cleaned_data

class PredictionFilterForm(forms.Form):
    """
    Formulaire pour rechercher et filtrer les prédictions.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Juste pour que django ne m'embète pas pour la première migration
        """
        super().__init__(*args, **kwargs)
        try:
            # Charge dynamiquement les choix de modèles de régression
            reg_models = Reg_model.objects.all()
            self.fields['reg_model'].choices = [("", "Tous")] + [(model.name, model.name) for model in reg_models]
        except OperationalError:
            # Si la table n'existe pas encore (par ex. lors des migrations), on laisse le champ vide
            self.fields['reg_model'].choices = [("", "Tous")]
    
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
                               choices=[],
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


