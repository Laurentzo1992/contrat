from django.urls import path
from . import views
urlpatterns = [
        #Leave as empty string for base url
    path('gestioncontrat/contrat', views.contrat, name="contrat"), 
    path('gestioncontrat/add', views.add_contrat, name="add_contrat"),
    path('gestioncontrat/edit/<int:id>', views.edit_contrat, name="edit_contrat"),
    path('gestioncontrat/delete/<int:id>', views.delete_contrat, name="delete_contrat"),  
]