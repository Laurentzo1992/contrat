from django.db import models
from gestioncontrat.models import Type, Partenaire, Structure

class Convention(models.Model):
    
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)
    partenaire = models.ForeignKey(Partenaire, on_delete=models.CASCADE, null=True, blank=True)
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, null=True, blank=True)
    reference = models.CharField(max_length=10)
    objet = models.TextField(null=True, blank=True)
    montant = models.FloatField()
    duree = models.CharField(max_length=10)
    date_signature = models.DateField(null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    nombre_renouv = models.IntegerField(null=True, blank=True)
    date_renouvel = models.DateField(null=True, blank=True)
    date_alerte = models.DateField(null=True, blank=True)
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
