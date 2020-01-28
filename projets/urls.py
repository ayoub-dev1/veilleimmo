from django.urls import  path
from .views import  CreateProjectVie

app_name = 'projects'

urlpatterns = [
    path('ajouterproject', CreateProjectVie.as_view(), name="ajouter")
]