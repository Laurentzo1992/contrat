from typing import Type
from django.contrib import admin
from gestioncontrat.models import Travail, Structure, Partenaire, Type

admin.site.register(Travail)
admin.site.register(Partenaire)
admin.site.register(Structure)
admin.site.register(Type)


# Register your models here.
