from django.urls import path
from . import views
urlpatterns = [
        #Leave as empty string for base url
    path('convention', views.convention, name="convention"),
    path('convention/add', views.convention_add, name="convention_add"),
    path('convention/edit/<int:id>', views.convention_edit, name="convention_edit"),
    path('convention/delete/<int:id>', views.convention_delete, name="convention_delete"),
    path('convention/archive/<int:id>', views.archive, name="archive_conv"),
    
    path('convention/type_con', views.type_con, name="type_con"),
    path('convention/type_conv/add/', views.add_type_con, name="add_type_con"),
    path('convention/type_conv/edit/<int:id>', views.edit_type_con, name="edit_type_con"),
    path('convention/type_conv/delete/<int:id>', views.delete_type_con, name="delete_type_con"),
     
]