from django.db import models
from promoteurs.models import Promoteur
from marques.models import  Marque




class Projet(models.Model):
    nom_projet = models.CharField(max_length=128)
    image_logo = models.ImageField(upload_to='projects/%Y/%m/%d')
    nom_promoteur = models.ForeignKey(Promoteur, on_delete=models.CASCADE)
    marque = models.ForeignKey(Marque, on_delete=models.DO_NOTHING, null=True, blank=True)
    region = models.CharField(max_length=128, null=True, blank=True)
    region1 = models.CharField(max_length=128, null=True, blank=True)
    region2 = models.CharField(max_length=128, null=True, blank=True)
    region3 = models.CharField(max_length=128, null=True, blank=True)
    superficie = models.IntegerField()
    localisation = models.CharField(max_length=128, null=True, blank=True)
    consistance = models.IntegerField()
    annee_lancement = models.DateTimeField()

    def __str__(self):
        return str(self.nom_projet)

    # add localisation , 
    # dans Promoteur : add image de logo 
    # dans Marque : add image de logo 
    # dans Offre : add gallerie image  
    # dans Projet : add gallerie image  






    

