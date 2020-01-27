from django.db import models
from promoteurs.models import Promoteur


class Projet(models.Model):
    nom_projet = models.CharField(max_length=128)
    nom_promoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE)
    region = models.CharField(max_length=128)
    region1 = models.CharField(max_length=128)
    region2 = models.CharField(max_length=128)
    region3 = models.CharField(max_length=128)
    superficie = models.IntegerField()
    consistance = models.CharField(max_length=128)
    annee_lancement = models.TimeField()

    # add localisation , 
    # dans Promoteur : add image de logo 
    # dans Marque : add image de logo 
    # dans Offre : add gallerie image  
    # dans Projet : add gallerie image  






    

