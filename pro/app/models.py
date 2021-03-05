from django.db import models

# Create your models here.
class jock(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(max_length=15)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    