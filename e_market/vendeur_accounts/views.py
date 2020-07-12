from django.shortcuts import render
from .forms import ProductForm

# Create your views here.
def accueil(request):
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
        envoi = True
        form.save()
    return render(request, 'vendeur_accounts/home.html', locals())


#def formulaire(request):
    #form = ProductForm(request.POST or None)
    #if form.is_valid():
        #envoi = True
        #form.save()

    #return render(request, 'vendeur_accounts/home.html', locals())

