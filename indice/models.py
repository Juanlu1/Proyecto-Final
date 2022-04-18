from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    first_name = models.CharField(max_length=40,null=True)
    last_name = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=50)
    description = models.CharField(max_length=150, null=True)