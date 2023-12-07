from django.db import models

# Create your models here.
class Users(models.Model):
    login = models.CharField(max_length=100) # username or email
    password = models.CharField(max_length=50) # encryption ?
