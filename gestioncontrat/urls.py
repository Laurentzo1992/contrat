from django.urls import path
from . import views
urlpatterns = [
        #Leave as empty string for base url
    path('contrat', views.contrat, name="contrat"), 
    path('add', views.add, name="add"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),  
]