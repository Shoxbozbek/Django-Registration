from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomeUser(AbstractUser):
    pass


class LeadRegister (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name