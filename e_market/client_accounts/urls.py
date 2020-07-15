from django.urls import path
from .views import accueil_client
from .views import detail_produit
from .views import connexion

urlpatterns = [
    path('client', accueil_client),
    path('detail/<uuid:uuid>', detail_produit, name='detail'),
    path('connexion_client', connexion, name='connexion_client')
]