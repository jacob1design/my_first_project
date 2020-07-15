from django.shortcuts import render, get_object_or_404
from vendeur_accounts.models import Produit
from django.contrib.auth import login, authenticate
from .forms import ConnexionForm

# Create your views here.
def accueil_client(request):
    produit = Produit.objects.all()

    return render(request, 'client/home.html', locals())


def detail_produit(request, uuid):
    detail = get_object_or_404(Produit, uuid=uuid)

    return render(request,'client/detail_produit.html', locals())

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            user = authenticate(user_name=user_name, password=password)

            if user :
                login(request, user)
            else :
                error = True

    else :
        form = ConnexionForm()

    return render(request, 'client/connexion.html', locals())