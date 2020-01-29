from django.db import models





class Categorie(models.Model):
    nom_categorie                  = models.CharField(max_length=128)
    update                         = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp            = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.nom_categorie