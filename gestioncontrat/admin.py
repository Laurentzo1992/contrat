from django.contrib import admin
from gestioncontrat.models import Travail, Financement, Categorie, Structure, Partenaire


admin.site.register(Travail)
admin.site.register(Categorie)
admin.site.register(Partenaire)
admin.site.register(Structure)
admin.site.register(Financement)

# Register your models here.
