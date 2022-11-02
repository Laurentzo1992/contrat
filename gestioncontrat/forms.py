from django import forms
from gestioncontrat.models import Travail, Structure, Partenaire, Type
from django.core.validators import RegexValidator


### FORM CONTRAT ###

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
        
        
### FORM Structure ###   

class Structureform(forms.ModelForm):
    
    sigle = forms.CharField(
        label='Signle',
        validators=[RegexValidator(r'^[A-Z0-9]*$',
        message="Lettre majuscule et chiffre autorisé")],
        widget=forms.TextInput(attrs={'placeholder': 'Signe'})
    )
    
    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom'})
    )
    
    class  Meta:
        model = Structure
        fields = '__all__'
        
        
        
### FORM Partenaire ###    

class PartenaireForm(forms.ModelForm):

    email = forms.CharField(
        label='Signle',
        validators=[RegexValidator(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',
        message="Value of Email not correct")],
        widget=forms.TextInput(attrs={'placeholder': 'Email'})
    )
    
    nom = forms.CharField(
        label='Nom',
        widget=forms.TextInput(attrs={'placeholder': 'Nom'})
    )
    
    class  Meta:
        model = Partenaire
        fields = '__all__'
        


### FORM TYPE CONTRAT ###    

class TypeForm(forms.ModelForm):
    
    libelle = forms.CharField(
        label='Libele',
        widget=forms.TextInput(attrs={'placeholder': 'Libele'})
    )
    
    class  Meta:
        model = Type
        fields = '__all__'