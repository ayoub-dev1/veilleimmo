from django.shortcuts import render

from django.views.generic import  CreateView
from .forms import  CreatProjectForm
from django.contrib.messages.views import SuccessMessageMixin

class CreateProjectVie(CreateView):
    form_class = CreatProjectForm
    template_name = "projets/ajouterproject.html"
    success_url = '/'
    success_message = " bien enregistrés"
