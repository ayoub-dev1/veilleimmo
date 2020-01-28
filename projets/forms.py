from django import  forms
from projets.models import  Projet




class CreatProjectForm(forms.ModelForm):
    class Meta:
        model =  Projet
        fields  = ['nom_projet', 'nom_promoteur', 'region',
                     'region1', 'region2','region3', 'superficie',
                     'consistance', 'annee_lancement']
    