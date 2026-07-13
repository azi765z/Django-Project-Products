from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    ROLE_CHOICES = (("admin", "Admin"),("user", "User"),  ("seller", "Seller"))
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default="user")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)