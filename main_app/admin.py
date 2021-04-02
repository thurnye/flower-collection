from django.contrib import admin

# Register your models here.
from .models import Flower, Meal, Vase

# Register your models here
admin.site.register(Flower)
admin.site.register(Meal)
admin.site.register(Vase)