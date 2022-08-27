from django.db import models

# Create your models here.
class Dealership(models.Model):
    name = models.CharField(max_length = 225)
    adress = models.CharField(max_length = 225)