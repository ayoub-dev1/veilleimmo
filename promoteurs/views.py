from django.shortcuts import render
from django.views.generic import  CreateView
from promoteurs.forms import  CreationMarqueForm
from django.contrib.messages.views import  SuccessMessageMixin



class CreatePromoteurView(SuccessMessageMixin,CreateView):
    form_class    = CreationMarqueForm
    template_name = 'promoteurs/ajouterpromoteur.html' 
    success_url = '/'
    success_message = "promoteur a ete bien enregistré "


