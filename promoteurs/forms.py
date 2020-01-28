from django import  forms
from django.views.generic import  CreateView
from .models import  Promoteur
   



class CreationMarqueForm(forms.ModelForm):
    class Meta:
        model = Promoteur
        fields = ['nom', 'prenom', 'site_web', 'adress']
        widgets = {
            'nom': forms.TextInput(attrs={'class':'form-control simple'}),
            'prenom': forms.TextInput(attrs={'class':'form-control simple'}),
            'site_web': forms.TextInput(attrs={'class':'form-control simple'}),
            'adress': forms.Textarea(attrs={'class':'form-control simple',}),
        }