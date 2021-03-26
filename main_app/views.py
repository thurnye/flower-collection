from django.shortcuts import render
from django.http import HttpResponse



# Define the about view
def home(request):
  return render (request, 'about.html')


# Flower Page
def flower_index(request):
  return render (request, 'flower/flowers.html')


