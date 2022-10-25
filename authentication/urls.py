from  django.urls import  path
from  . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('login_user', views.login_user, name="login_user"),
    path('auth/logout_user', views.Logout_user, name='logout_user'),
    path('auth/profile', views.profile, name='profile'),
    path('home', views.home, name='home'),
    path('auth/add', views.add, name="add"),
    path('auth/edit/<int:id>', views.edit, name="edit"),
    path('auth/delete/<int:id>', views.delete, name="delete"),
    path('auth/users', views.users, name="users"),
    path('auth/statistique', views.statistique, name="statistique"),
    
]
