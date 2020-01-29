from django.shortcuts import render

from django.views.generic import  CreateView
from .forms import  CreatProjectForm
from django.contrib.messages.views import SuccessMessageMixin

class CreateProjectVie(CreateView):
    form_class = CreatProjectForm
    template_name = "projets/ajouterproject.html"
    success_url = '/'
    success_message = " bien enregistrés"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        request = self.request
        print(request)
        return super().form_valid(form)
