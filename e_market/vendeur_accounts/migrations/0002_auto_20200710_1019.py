# Generated by Django 2.2.13 on 2020-07-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendeur_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='cover',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]