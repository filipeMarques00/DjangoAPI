from django.db import models
from uuid import uuid4

# Create your models here.

class Users(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    
    
    
    
    
    
    
    
    
    
    
