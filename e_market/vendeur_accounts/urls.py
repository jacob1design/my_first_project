from django.urls import path
from .views import accueil
#from .views import formulaire


urlpatterns = [
    path('', accueil, name='save_product'),
   # path('formulaire/', formulaire, name='save_product')
]