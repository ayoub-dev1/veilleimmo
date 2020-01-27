from django.db import models
from promoteurs.models import Promoteur

class Marque(models.Model):
    promoteur = models.ForeignKey(Promoteur, on_delete=models.DO_NOTHING)
    nom_marque = models.CharField(max_length=64)
    site_web = models.CharField(max_length=255)
    adresse_siege_social = models.TextField(max_length=128)


    def __str__(self):
        return str(self.nom_marque)
    