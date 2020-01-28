from django.urls import  path
from .views import  CreatePromoteurView


app_name = 'promoteurs'

urlpatterns = [
    path('ajouterpromoteur', CreatePromoteurView.as_view(), name="ajouter")
]