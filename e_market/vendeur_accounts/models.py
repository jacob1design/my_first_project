from django.db import models
import uuid

# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Produit(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    nom = models.CharField(max_length=15)
    description = models.TextField()
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to="photo/",null=True)
    created_at = models.DateTimeField(auto_now=True)
    last_modification = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, models.PROTECT, null=True)


    def __str__(self):
        return self.nom

