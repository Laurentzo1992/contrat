from django.urls import path
from . import views
urlpatterns = [
        #Leave as empty string for base url
    path('gestioncontrat/contrat', views.contrat, name="contrat"), 
    path('gestioncontrat/add', views.add_contrat, name="add_contrat"),
    path('gestioncontrat/edit/<int:id>', views.edit_contrat, name="edit_contrat"),
    path('gestioncontrat/delete/<int:id>', views.delete_contrat, name="delete_contrat"),
    path('gestioncontrat/structure', views.structure, name="structure"), 
    path('gestioncontrat/structure/add', views.add_struct, name="add_struct"),
    path('gestioncontrat/structure/edit/<int:id>', views.edit_struct, name="edit_struct"),
    path('gestioncontrat/sturcture/delete/<int:id>', views.delete_struct, name="delete_struct"),
    path('gestioncontrat/partenaire', views.partenaire, name="partenaire"), 
    path('gestioncontrat/partenaire/add', views.add_part, name="add_part"),
    path('gestioncontrat/partenaire/edit/<int:id>', views.edit_part, name="edit_part"),
    path('gestioncontrat/partenaire/delete/<int:id>', views.delete_part, name="delete_part"),   
]