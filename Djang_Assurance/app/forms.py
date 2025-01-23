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
        exclude = ['result']



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
        exclude = ['result', 'reg_model']
