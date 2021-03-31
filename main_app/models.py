from django.db import models
from django.urls import reverse

# Create your models here.
class Flower (models.Model) :
    name =  models.CharField(max_length=50)
    species =  models.CharField(max_length=50)
    description =  models.TextField(max_length=250)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})
