from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=2883)