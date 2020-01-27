from django import  forms
from .models import  Marque


class MarqueForm(forms.ModelForm):
    class Meta:
        model = Marque
        fields  = ['promoteur', 'nom_marque', 'site_web', 'adresse_siege_social']
        widgets = {
            'adresse_siege_social': forms.Textarea(attrs={'class':'form-control simple'}),
            'nom_marque': forms.TextInput(attrs={'class':'form-control simple'}),
            'site_web': forms.TextInput(attrs={'class':'form-control simple'}),
            'promoteur': forms.TextInput(attrs={'class':'form-control simple', "type":"hidden"}),
        }

    
    # def clean_promoteur(self):
    #     data = self.cleaned_data
    #     promoteur = data['promoteur']
    #     if promoteur is None:
    #         raise forms.ValidationError('No')
    #     promoteur = request.user
    #     return promoteur


