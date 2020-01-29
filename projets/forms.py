from django import  forms
from projets.models import  Projet




class CreatProjectForm(forms.ModelForm):
    class Meta:
        model =  Projet
        fields  = ['nom_projet', 'nom_promoteur',
                     'region1', 'region2','region3', 'superficie',
                     'consistance', 'annee_lancement', 'marque', 'image_logo']
        widgets = {
            'nom_projet': forms.TextInput(attrs={'class':'form-control simple'}),
            'region1': forms.TextInput(attrs={'class':'form-control simple'}),
            'region2': forms.TextInput(attrs={'class':'form-control simple'}),
            'region3': forms.TextInput(attrs={'class':'form-control simple'}),
            'consistance': forms.TextInput(attrs={'class':'form-control simple'}),
            'superficie': forms.NumberInput(attrs={'class':'form-control simple'}),
            'annee_lancement': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'nom_promoteur': forms.Select(attrs={'class':'form-control simple selectmultiply'}),
            'image_logo': forms.FileInput(attrs={'class':'form-control simple selectmultiply'}),
            'marque': forms.Select(attrs={'class':'form-control simple selectmultiply'})
        }