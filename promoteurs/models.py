from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.conf import settings
User = get_user_model()

class Promoteur(models.Model):
    nom    = models.CharField(max_length=255)
    prenom    = models.CharField(max_length=255)
    site_web = models.URLField()
    adress    = models.CharField(max_length=255)

    def __str__(self):
        return "{nom}  {prenom}".format(nom=self.nom, prenom=self.prenom)

# def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             Promoteur.objects.create(user=instance)
#         except:
#             pass


# post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)