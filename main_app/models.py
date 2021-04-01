from django.db import models
from django.urls import reverse



GROWTH = (
    ('SL', 'Sunlight'),
    ('PT', 'Proper Temperature'),
    ('MT', 'Moisture'),
    ('A', 'Air'),
    ('NT', 'Nutrients'),
)


# Create your models here.
class Flower (models.Model) :
    name =  models.CharField(max_length=50)
    species =  models.CharField(max_length=50)
    description =  models.TextField(max_length=250)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})    

# Add the new Model for the meal
class Meal(models.Model):
    date = models.DateField('Period')
    growth = models.CharField(
        max_length=2,
        choices=GROWTH,
        default=GROWTH[0][0],
    )
    # addition of the foreign key for the one to many relations
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_growth_display()} on {self.date}"
        
    # change the default sort
    class Meta:
        ordering = ['-date']