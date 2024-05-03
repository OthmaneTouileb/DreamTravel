from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):

    email = models.EmailField(unique=True)
    Fullname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['Fullname', 'username']
    
    def __str__(self):
        return self.Fullname
    
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')
