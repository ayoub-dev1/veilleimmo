from django import  forms
from .models import   Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'fonction', 'telephone','email']
    

        widgets = {
            'nom': forms.TextInput(attrs={"class":"form-control simple"}),
            'prenom': forms.TextInput(attrs={"class":"form-control simple"}),
            'telephone': forms.Textarea(attrs={"class":"form-control simple"}),
            'email': forms.TextInput(attrs={"class":"form-control simple"}),
        }