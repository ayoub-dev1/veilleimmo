from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import  home
from accounts.views import  LoginView, RegisterPromoreurView,RegisterPromoreur
from django.contrib.auth.views import LogoutView
from contacts.views import  SendContactForm

from offres.views import  CreateFormView,loadBien

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),

    #Account
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('ajouterutilisateur/',RegisterPromoreurView.as_view(), name="ajouter-utilisateur"),

    #Contact
    path('contact/', SendContactForm.as_view(), name="contact"),
    #Marque
    path('marques/', include('marques.urls',namespace="marque")),

    #Promoteurs
    path('promoteur/', include('promoteurs.urls', namespace="promoteurs")),

    #Project
    path('projects/', include('projets.urls', namespace="projects")),

    #Offres
    path('offre/ajouter/', CreateFormView.as_view(), name="ajouter-offre"),
    path('ajax/loads-bien',loadBien , name="loads-biens")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
