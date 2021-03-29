from django.db import models

# Create your models here.
class Flower (models.Model) :
    name =  models.CharField(max_length=50)
    species =  models.CharField(max_length=50)
    description =  models.TextField(max_length=250)