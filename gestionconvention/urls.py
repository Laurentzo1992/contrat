from django.urls import path
from . import views
urlpatterns = [
        #Leave as empty string for base url
    path('convention', views.convention, name="convention"),
    path('convention/add', views.convention_add, name="convention_add"),
    path('convention/edit/<int:id>', views.convention_edit, name="convention_edit"),
    path('convention/delete/<int:id>', views.convention_delete, name="convention_delete"),  
]