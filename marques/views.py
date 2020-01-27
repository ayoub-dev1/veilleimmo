from django.shortcuts import render, redirect
from django.views.generic import  ListView,CreateView
from promoteurs.models import  Promoteur
from .models import  Marque
from .forms import  MarqueForm





class ListMarque(ListView):
    model = Marque
    queryset = Marque.objects.all()
    template_name = 'marques/listmarque.html'

    def get(self, request, *args, **kwargs):
        print(request.session.items())
        return render(request, self.template_name)


class CreateMarqueView(CreateView):
    form_class = MarqueForm
    template_name = 'marques/ajoutermarque.html'
    success_url = '/'

    def get_initial(self, *args, **kwargs):
        request = self.request
        initial = super(CreateMarqueView,self).get_initial(**kwargs)
        initial['promoteur'] = request.user
        print(request)
        print(request.POST)
        return initial
