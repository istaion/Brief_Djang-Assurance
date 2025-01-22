from django.db import models
from django.contrib.auth.models import User

class Reg_model(models.Model):
    name = models.CharField(max_length=200)
    path = models.FilePathField()

    def __str__(self):
        return self.titre
    

class Prediction(models.Model):
    result = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_model = models.ForeignKey(Reg_model, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return "prédiction de l'utilisateur : " + str(self.user_id) + "avec un résultat de : " + str(self.result)
