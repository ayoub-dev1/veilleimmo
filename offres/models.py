from django.db import models
from projets.models import Projet
from categories.models import  Categorie


class TypeBien(models.Model):
    nom_type_bien = models.CharField(max_length=64)
    update        = models.DateTimeField(auto_now=True, auto_now_add=False)
    categorie     = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.nom_type_bien) + " to " + str(self.categorie)


# Offre : Residentiel, Foncier , Commerce
class Offre(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    type_bien = models.ForeignKey(TypeBien, on_delete=models.DO_NOTHING)
    superfecie_min = models.IntegerField()
    superfecie_max = models.IntegerField()
    id_project = models.ForeignKey(Projet, on_delete=models.DO_NOTHING)
    #avantages : piscine , asc, parquet , armoire , 



class SubOffers(models.Model):
    prix_metre = models.FloatField()
    prix_min = models.FloatField()
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    existence_de_noire = models.BooleanField(default=False)
    noir_montant = models.IntegerField()



# standing ; valable que pour la categorie Residentiel , il accept Trois valeurs (Moyen , economique, haut standing )

UTILISATION_RDC =(
    ('habitaion', 'Habitaion'),
    ('commercial', 'Commercial'),

)

class Pricing(models.Model):
    id_offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    prix_metre = models.FloatField()
    prix_min = models.FloatField()
    prix_max = models.FloatField()
    existence_noire = models.BooleanField()
    montant_noire = models.FloatField()
    pourcentage_noire = models.FloatField()
    nombre_piece = models.IntegerField()
    etage   = models.IntegerField()
    elevation_immeuble = models.IntegerField()
    vis_a_vis =  models.CharField(max_length=255)
    nombre_facade = models.IntegerField()
    utilisation_RDC = models.CharField(max_length=128, choices=UTILISATION_RDC)

class ModalitePaiment(models.Model):
    id_offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    versement_1 = models.IntegerField()
    pourcentage_versement1 = models.IntegerField()
    versement_2 = models.IntegerField()
    pourcentage_versement2 = models.IntegerField()
    versement_3 = models.IntegerField()
    pourcentage_versement3 = models.IntegerField()
    versement_4 = models.IntegerField()
    pourcentage_versement4= models.IntegerField()
    nombre_piece = models.IntegerField()
    etage   = models.IntegerField()
    elevation_immeuble = models.IntegerField()
    vis_a_vis =  models.CharField(max_length=255)
    nombre_facade = models.IntegerField()
    utilisation_RDC = models.CharField(max_length=128, choices=UTILISATION_RDC)



