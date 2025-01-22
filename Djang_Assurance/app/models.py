from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import pandas as pd
import cloudpickle

SEX_CHOICES =( 
    ("female", "Femme"), 
    ("male", "Homme")
) 

SMOKER_CHOICES =( 
    ("yes", "Oui"), 
    ("no", "Non")
) 

REGION_CHOICES =( 
    ("southeast", "Sud Est"), 
    ("southwest", "Sud Ouest"),
    ("northeast", "Nord Est"), 
    ("northwest", "Nord Ouest")
) 

class Reg_model(models.Model):
    name = models.CharField(max_length=200)
    path = models.FilePathField(path='app/regression/models/')

    def calcul_prediction(self, age, sex, weight, size, children, smoker, region):
        bmi = weight / pow(size / 100, 2)
        data = pd.DataFrame(
            data=[[age, sex, bmi, children, smoker, region]],
            columns=["age", "sex", "bmi", "children", "smoker", "region"]
        )
        with open(self.path, 'rb') as f:
            reg = cloudpickle.load(f)
        prediction = reg.predict(data)
        return prediction

    def __str__(self):
        return self.name
    

class Prediction(models.Model):
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(130)], default =10)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default="female")
    weight = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(300)], default =60)
    size = models.FloatField(validators=[MinValueValidator(30), MaxValueValidator(300)],default =170)
    children = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], default = 5)
    smoker	= models.CharField(max_length=3, choices=SMOKER_CHOICES, default="no")
    region = models.CharField(max_length=9, choices=REGION_CHOICES, default="northwest")
    result = models.FloatField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_model = models.ForeignKey(Reg_model, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return "prédiction de l'utilisateur : " + str(self.user_id) + "avec un résultat de : " + str(self.result)
    
    def pred(self):
        pred = self.reg_model.calcul_prediction(self.age, self.sex, self.weight, self.size, self.children, self.smoker, self.region)[0]
        self.result = pred
