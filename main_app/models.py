from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User








# Vase Model
class Vase (models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vase_detail', kwargs={'pk': self.id})



# Flower Model
class Flower (models.Model) :
    name =  models.CharField(max_length=50)
    species =  models.CharField(max_length=50)
    description =  models.TextField(max_length=250)
    # Add the M:M relationship
    vases = models.ManyToManyField(Vase)
    # Link the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})    





# Meal Model
GROWTH = (
    ('SL', 'Sunlight'),
    ('PT', 'Proper Temperature'),
    ('MT', 'Moisture'),
    ('A', 'Air'),
    ('NT', 'Nutrients'),
)
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


