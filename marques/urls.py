from django.urls import  path
from .views import  CreateMarqueView,ListMarque
app_name = 'marque'
urlpatterns = [
    path('',ListMarque.as_view(), name="list-marques"),
    path('ajouter',CreateMarqueView.as_view(), name="ajouter-marque"),
]