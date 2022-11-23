from django import forms
from gestionconvention.models import Convention
from django.core.validators import RegexValidator


### FORM CONTRAT ###

class ConventionForm(forms.ModelForm):
    
    reference = forms.CharField(
        label='Reference', min_length=2, max_length=100,
        validators=[RegexValidator(r'^[A-Z0-9]*$',
        message="Lettre majuscule et chiffre autorisé")],
        widget=forms.TextInput(attrs={'placeholder': 'Réference'})
    )
    
    objet = forms.CharField(
        label='Objet', min_length=2, max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Objet du contrat'})
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
        model = Convention
        fields = '__all__'