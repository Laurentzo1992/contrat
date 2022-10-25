from django.db import models

class Partenaire(models.Model):
    nom = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nom
    
    
class Structure(models.Model):
    sigle = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)


    def __str__(self):
        return self.sigle

class Financement(models.Model):
    intitule = models.CharField(max_length=100)
    
    def __str__(self):
        return self.intitule
    
class Categorie(models.Model):
    intitule = models.CharField(max_length=100)

    
    def __str__(self):
        return self.intitule
    
    
class Travail(models.Model):
     
    reference = models.CharField(max_length=10)
    objet = models.TextField()
    nature = models.CharField(max_length=100)
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=80)
    montant = models.FloatField()
    duree = models.CharField(max_length=10)
    date_signature = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    nombre_renouv = models.IntegerField()
    date_renouvel = models.DateField()
    lieu = models.CharField(max_length=100)
    date_alerte = models.DateField()
    file = models.FileField(upload_to='uploads_files/', blank=True)
    created_at =models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.reference
    
    @property
    def fileURL(self):
        try:
            url = self.file.url
        except:
            url = ''
        return url


# Create your models here.
