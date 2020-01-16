from django.db import models
from django.contrib.auth.models import User

class Gift(models.Model) :

    item = models.CharField(max_length=50)
    description = models.TextField()
    

class UserProfile(models.Model) :

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField(default=0)
    gift = models.ForeignKey(Gift,on_delete=models.CASCADE)

