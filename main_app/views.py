from django.shortcuts import render
from django.http import HttpResponse
from .models import Flower



# Define the about view
def home(request):
    return render (request, 'about.html')


# Flower Page
def flower_index(request):
    flowers = Flower.objects.all()
    print(flowers)
    return render (request, 'flower/flowers.html', { 'flowers': flowers })

# Single Flower detail
def flower_detail(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    return render (request, 'flower/detail.html', {"flower": flower})