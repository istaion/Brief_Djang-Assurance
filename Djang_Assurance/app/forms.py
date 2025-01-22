from django import forms

SEX_CHOICES =( 
    ("female", "Femme"), 
    ("male", "Homme")
) 

SEX_CHOICES =( 
    ("yes", "Oui"), 
    ("no", "Non")
) 

REGION_CHOICES =( 
    ("southeast", "Sud Est"), 
    ("southwest", "Sud Ouest"),
    ("northeast", "Nord Est"), 
    ("northwest", "Nord Ouest")
) 

class PredictionForm(forms.Form):
    age = forms.IntegerField(min_value=0, max_value=130)
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    weight = forms.FloatField(min_value=0.1,max_value=300)
    size = forms.FloatField(min_value=1,max_value=300)
    children = forms.IntegerField(min_value=0, max_value=30)
    smoker	= forms.ChoiceField(choices=SEX_CHOICES)
    region = forms.ChoiceField(choices=REGION_CHOICES)