from django.urls import path
from .views import accueil_client

urlpatterns = [
    path('client', accueil_client)
]