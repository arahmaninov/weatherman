from django.db import models
from user.models import Users

# Create your models here.
class Locations(models.Model):
    name = models.CharField(max_length=255)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=7)
    longitude = models.DecimalField(max_digits=12, decimal_places=7)
    
    def __str__(self):
        return self.name

