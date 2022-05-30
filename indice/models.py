from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    more_description = models.CharField(max_length=150, null=True, default= "")
    link = models.CharField(max_length=300, null=True, default= "")
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True, default= "")
    user = models.ForeignKey(User, on_delete=models.CASCADE)