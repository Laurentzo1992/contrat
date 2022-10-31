from django.db import models


##### Model Partenaire #####

class Partenaire(models.Model):
    nom = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.nom
    
    
    
##### Model Structure #####

class Structure(models.Model):
    sigle = models.CharField(max_length=100, null=True, blank=True)
    nom = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.sigle
    
    
    
##### Model Type #####

class Type(models.Model):
    libelle = models.CharField(max_length=70, null=True, blank=True)

    def __str__(self):
        return self.libelle
     


##### Model Contrat #####
 
class Travail(models.Model):
    
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE, null=True, blank=True)
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, blank=True)
    reference = models.CharField(max_length=10)
    objet = models.TextField(null=True, blank=True)
    nature = models.CharField(max_length=100, null=True, blank=True)
    matricule = models.CharField(max_length=10, null=True, blank=True)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=80)
    montant = models.FloatField()
    duree = models.CharField(max_length=10)
    date_signature = models.DateField(null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    nombre_renouv = models.IntegerField(null=True, blank=True)
    date_renouvel = models.DateField(null=True, blank=True)
    lieu = models.CharField(max_length=100, null=True, blank=True)
    date_alerte = models.DateField()
    file = models.FileField(upload_to='uploads_files/', null=True, blank=True)
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
