from django.shortcuts import render
import os
from django.views.generic import FormView
from .forms import PredictionForm
import pickle
import cloudpickle
import pandas as pd
import sklearn
from app.regression.regression_model import AgeTransformer, BmiTransformer



# def calcul_prediction(age, sex, weight, size, children, smoker, region):
#     from app.regression.regression_model import AgeTransformer, BmiTransformer
#     bmi = weight/pow(size/100,2)
#     data = pd.DataFrame(data = [[50,"female",27,0,"yes","northwest"]],columns=["age","sex","bmi","children","smoker","region"])
#     print(data)
#     with open('app/regression/best_lasso_model.pkl', 'rb') as f:
#         reg= pickle.load(f)
#     reg.predict(data)

def calcul_prediction(age, sex, weight, size, children, smoker, region):
    from app.regression.regression_model import AgeTransformer, BmiTransformer  # Import des classes nécessaires

    bmi = weight / pow(size / 100, 2)
    data = pd.DataFrame(
        data=[[age, sex, bmi, children, smoker, region]],
        columns=["age", "sex", "bmi", "children", "smoker", "region"]
    )
    print(data)
    
    # Charger le modèle avec les imports nécessaires pour pickle
    with open('app/regression/best_lasso_model.pkl', 'rb') as f:
        reg = cloudpickle.load(f)
    prediction = reg.predict(data)
    return prediction

class PredictionView(FormView):
    template_name = 'app/prediction.html'
    form_class = PredictionForm
    print("C'est laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa :", calcul_prediction(50,"female",80,160,0,"yes","northwest"))
    # def get_queryset(self):
    #     form = self.form_class(self.request.GET)
    #     queryset = Article.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    # def get(self, request, *args, **kwargs):
    #     with open('Hacene/modele de regresion lineaire.pkl', 'rb') as f:
    #         reg= pickle.load(f)
    #     return super().get(request, *args, **kwargs)

# class CreerArticleView(CreateView):
#     model = Article
#     form_class = ArticleForm
#     template_name = 'blog/creer_article.html'
#     success_url = reverse_lazy('liste_articles')