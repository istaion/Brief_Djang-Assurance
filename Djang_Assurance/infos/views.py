from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class NewsView(TemplateView):
    template_name = 'infos/news.html'