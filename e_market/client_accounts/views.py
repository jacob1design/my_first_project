from django.shortcuts import render
from vendeur_accounts.models import Produit

# Create your views here.
def accueil_client(request):
    produit = Produit.objects.all()

    return render(request, 'client/home.html', locals())

