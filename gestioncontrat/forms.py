from dataclasses import fields
from pyexpat import model
from django import forms
from gestioncontrat.models import Travail
from django.core.validators import RegexValidator

class TravailForm(forms.ModelForm):
    
    reference = forms.CharField(
        label='Reference', min_length=2, max_length=100,
        validators=[RegexValidator(r'^[A-Z0-9]*$',
        message="Lettre majuscule et chiffre autorisé")],
        widget=forms.TextInput(attrs={'placeholder': 'Réference'})
    )
    
    nature = forms.TypedChoiceField(
        label='Nature',
        choices = (("CDD", "CDD"), ("CDI", "CDI")),
        initial = 'CDD',
        required = True,
        widget = forms.Select,
    )
    
    objet = forms.CharField(
        label='Objet', min_length=2, max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Objet du contrat'})
    )
    
    
    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom du contracté'})
    )
    
    prenom = forms.CharField(
        label='Prenom',
        widget=forms.TextInput(attrs={'placeholder': 'Prenom du contracté'})
    )
    
    date_signature = forms.DateField(
        label='Date de signature',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    
    date_debut = forms.DateField(
        label='Date debut de contrat',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    
    date_fin = forms.DateField(
        label='Date fin de contrat',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
     
    date_renouvel = forms.DateField(
        label='Date dernier renoulement',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    
    date_alerte = forms.DateField(
        label='Date alerte',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = Travail
        fields = '__all__'
        
    # reference = forms.CharField(max_length=10)
    # objet = forms.CharField()
    # nature = forms.CharField()
    # matricule = forms.CharField(max_length=10)
    # nom = forms.CharField(max_length=60)
    # prenom = forms.CharField(max_length=80)
    # montant = forms.FloatField()
    # duree = forms.CharField(max_length=10)
    # date_signature = forms.DateField()
    # date_debut = forms.DateField()
    # date_fin = forms.DateField()
    # nombre_renouv = forms.IntegerField()
    # date_renouvel = forms.DateField()
    # lieu = forms.CharField(max_length=100)
    # date_alerte = forms.DateField()
    # file = forms.FileField()
    # created_at =forms.DateField()
    # updated_at = forms.DateField()