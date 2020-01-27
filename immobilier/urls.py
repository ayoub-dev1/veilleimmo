from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import  home
from accounts.views import  LoginView, RegisterPromoreurView
from django.contrib.auth.views import LogoutView
from contacts.views import  SendContactForm

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),

    #Account
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('ajouterpromoteur/',RegisterPromoreurView.as_view(), name="ajouter-promoteur"),

    #Contact
    path('contact/', SendContactForm.as_view(), name="contact"),
    #Marque
    path('marques/', include('marques.urls',namespace="marque")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
