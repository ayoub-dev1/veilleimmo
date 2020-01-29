from django import  forms

from .models import  Offre, TypeBien



class OffreCreateForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ['categorie', 'type_bien', 'superfecie_min',
                     'superfecie_max',
                     'id_project']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['type_bien'].queryset = TypeBien.objects.none()
            
