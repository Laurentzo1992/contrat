from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    ADMINISTRATEUR = 'ADMINISTRATEUR'
    USER = 'USER'

    ROLE_CHOICES = (
        ('ADMINISTRATEUR', 'superadmin'),
        ('USER', 'user'),
    )
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='role')
    