from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from .models import ContactBase
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
class NewsView(TemplateView):
    template_name = 'infos/news.html'


class AboutView(TemplateView):
    template_name = 'infos/about.html'


class PrivacyView(TemplateView):
    template_name = 'infos/privacy.html'


class ContactView(FormView):
    template_name = 'infos/contact.html'
    form_class = ContactForm
    success_url=reverse_lazy('accueil')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        

    #     #succes
    #     messages.success(self.request, 'Merci pour votre message ! Nous y répondrons dans les plus brefs délais')
    #     return super().form_valid(form)
    
    # def form_invalid(self, form):
    #     #erreur
    #     messages.error(self.request, "Veuillez remplir correctement les champs")
    #     return super().form_invalid(form)