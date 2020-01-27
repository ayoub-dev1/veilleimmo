from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=128)
    prenom = models.CharField(max_length=128)
    email = models.EmailField()
    fonction = models.CharField(max_length=128,null=True,blank=True)
    telephone = models.CharField(max_length=10,null=True,blank=True)
    observation = models.TextField(null=True,blank=True)
    evaluation = models.IntegerField(null=True,blank=True)



    def __str__(self):
        return str(self.email)
    