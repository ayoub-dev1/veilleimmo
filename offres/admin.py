from django.contrib import admin
from .models import Offre,SubOffers, Pricing
# Register your models here.


admin.site.register(Offre)
admin.site.register(SubOffers)

admin.site.register(Pricing)