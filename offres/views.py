from django.shortcuts import render
from django.views.generic import  CreateView
from .forms import  OffreCreateForm

from .models import  TypeBien

# Create your views here.


class CreateFormView(CreateView):
    form_class = OffreCreateForm
    template_name = 'offres/ajouter.html'



def loadBien(request):
    catgory_id = request.GET.get('category')
    biens  = TypeBien.objects.filter(categorie=catgory_id).order_by('nom_type_bien')
    return render(request, 'offres/type_bien_drop_down.html', {'biens': biens})