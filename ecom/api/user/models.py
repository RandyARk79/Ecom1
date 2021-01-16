from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100, default='Anonymous')
    email = models.EmailField(max_length=100, unique=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=20, blank=True, null=True)
    gender = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Other', 'Other'),
        ("Don't Want to Say", 'None'),
    ]

    session_token = models.CharField(max_length=30, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __dir__(self):
        self.name + ":" + self.email
