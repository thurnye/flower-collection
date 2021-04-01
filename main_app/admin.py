from django.contrib import admin

# Register your models here.
from .models import Flower, Meal

# Register your models here
admin.site.register(Flower)
admin.site.register(Meal)