from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=2883)
    
    #create a Trait
class Trait(models.Model):
    height = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=8)
    weight = models.IntegerField()