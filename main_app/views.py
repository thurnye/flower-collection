from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower



# Define the about view
def home(request):
    return render (request, 'about.html')

# create
class CreateFlower(CreateView):
    model = Flower
    template_name = 'flower/add_form.html'
    fields = '__all__'
    success_url = '/flowers/'


# Get All
class GetAll(ListView):
    model= Flower
    template_name = 'flower/flowers.html'

# Get One
class FlowerDetail(DetailView) :
  model = Flower
  template_name = 'flower/detail.html'


# Edit One
class EditFlower(UpdateView):
    model = Flower
    template_name = 'flower/add_form.html'
    fields = '__all__'

class DeleteFlower(DeleteView):
    model = Flower
    template_name = 'flower/delete.html'
    success_url = '/flowers/'






