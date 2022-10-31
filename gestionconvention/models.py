from django.db import models


class Convention(models.Model):
     
    reference = models.CharField(max_length=10)
    objet = models.TextField()
    nature = models.CharField(max_length=100)
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=80)
    montant = models.FloatField()
    duree = models.CharField(max_length=10)
    date_signature = models.DateField(auto_now_add=True, null=False)
    date_debut = models.DateField()
    date_fin = models.DateField()
    nombre_renouv = models.IntegerField()
    date_renouvel = models.DateField()
    lieu = models.CharField(max_length=100)
    date_alerte = models.DateField()
    file = models.FileField(upload_to='uploads_files/', blank=True)
    created_at =models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
# Create your models here.
