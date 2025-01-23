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
    """
    Represents a machine learning regression model used for insurance predictions.

    Attributes:
        name (str): The name of the regression model.
        path (FilePathField): The file path where the serialized model is stored.
    """
    name = models.CharField(max_length=200,
                            help_text="The name of the regression model (e.g., 'Lasso Regression Model').")
    path = models.FilePathField(path='app/regression/models/',
                                help_text="The path to the serialized regression model file.")

    def calcul_prediction(self, age, sex, weight, size, children, smoker, region):
        """
        Calculates an insurance prediction using the regression model.

        Args:
            age (int): The user's age.
            sex (str): The user's gender ('male' or 'female').
            weight (float): The user's weight in kilograms.
            size (float): The user's height in centimeters.
            children (int): The number of children the user has.
            smoker (str): Whether the user is a smoker ('yes' or 'no').
            region (str): The user's residential region.

        Returns:
            float: The predicted insurance premium.
        """
        bmi = weight / pow(size / 100, 2)
        data = pd.DataFrame(
            data=[[age, sex, bmi, children, smoker, region]],
            columns=["age", "sex", "bmi", "children", "smoker", "region"]
        )
        print(data)
        print(data.dtypes)
        # Load the serialized regression model
        with open(self.path, 'rb') as f:
            reg = cloudpickle.load(f)
        prediction = reg.predict(data)
        return prediction

    def __str__(self):
        return self.name
    

class Prediction(models.Model):
    """
    Represents a user's prediction request and result.

    Attributes:
        age (int): The user's age (default: 10).
        sex (str): The user's gender ('male' or 'female', default: 'female').
        weight (float): The user's weight in kilograms (default: 60).
        size (float): The user's height in centimeters (default: 170).
        children (int): The number of children the user has (default: 5).
        smoker (str): Indicates if the user is a smoker ('yes' or 'no', default: 'no').
        region (str): The user's residential region (default: 'northwest').
        result (float): The predicted insurance premium (nullable).
        user_id (ForeignKey): Reference to the user associated with the prediction.
        reg_model (ForeignKey): The regression model used for prediction (nullable).
    """
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
    made_by_staff = models.BooleanField(default=False)



    def __str__(self):
        return f"prédiction de l'utilisateur : {self.user_id} avec un résultat de : {self.result}"
    
    def pred(self):
        """
        Calculate the insurance premium using the specified regression model or
        the most expensive prediction among all models.

        Returns:
            None: The result is stored in the `result` attribute.
        """
        if self.made_by_staff:
            pred = self.reg_model.calcul_prediction(self.age, self.sex, self.weight, self.size, self.children, self.smoker, self.region)[0]
        else:
            # If no specific regression model is chosen, use the most expensive prediction
            reg_models = Reg_model.objects.all()
            pred_list = []
            for model in reg_models:
                pred_list.append(model.calcul_prediction(self.age, self.sex, self.weight, self.size, self.children, self.smoker, self.region)[0])
            pred_list.sort()
            pred = pred_list[-1] # Choose the highest prediction
        self.result = round(pred,2)
    
    def fr_transform(self):
        """
        Transforms the prediction's fields into their French equivalent for better user display.

        Translates:
        - sex: 'male' -> 'homme', 'female' -> 'femme'
        - smoker: 'yes' -> 'oui', 'no' -> 'non'
        - region: English names to French names
        """
        match self.sex:
            case 'female': self.sex = 'femme'
            case 'male' :self.sex = 'homme'
        match self.smoker:
            case 'yes': self.smoker = 'oui'
            case 'no' : self.smoker = 'non'
        match self.region:
            case "southeast" : self.region = "Sud Est"
            case "southwest" : self.region = "Sud Ouest"
            case "northeast" : self.region = "Nord Est" 
            case "northwest" : self.region = "Nord Ouest"

