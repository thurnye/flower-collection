from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower, Vase
from .forms import MealForm



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
def FlowerDetail(request, pk):
    flower = Flower.objects.get(id=pk)
    # list all the vases in inventory
    vases_flower_doesnt_have = Vase.objects.exclude(id__in = flower.vases.all().values_list('id'))
    # instantiate MealForm to be rendered in the template
    meal_form = MealForm()
    return render(request, 'flower/detail.html', {
        'flower': flower, 
        'meal_form': meal_form,
        'vases' : vases_flower_doesnt_have
    })



# Edit One
class EditFlower(UpdateView):
    model = Flower
    template_name = 'flower/add_form.html'
    fields = '__all__'

class DeleteFlower(DeleteView):
    model = Flower
    template_name = 'flower/delete.html'
    success_url = '/flowers/'



def add_meal(request, pk):
    # create a ModelForm instance using the data in request.POST
    form = MealForm(request.POST)
    # validate the form
    if form.is_valid():
    # don't save the form to the db until it
    # has the pk assigned
        new_meal = form.save(commit=False)
        new_meal.flower_id = pk
        new_meal.save()
    return redirect('detail', pk=pk)


# Create Vase
class VaseCreate(CreateView):
    model = Vase
    template_name = 'flower/vase_form.html'
    fields = '__all__'

# get all vase tied with the flower
def assoc_vase(request, flower_id, vase_id):
  Flower.objects.get(id=flower_id).vases.add(vase_id)
  return redirect('detail', pk=flower_id)

# get all unassociated vase
def unassoc_vase(request, flower_id, vase_id):
  Flower.objects.get(id=flower_id).vases.remove(vase_id)
  return redirect('detail', pk=flower_id)

# list all vase
class VaseList(ListView):
  model = Vase
  template_name = 'flower/vase_list.html'


# vase detail
class VaseDetail(DetailView):
  model = Vase
  template_name = 'flower/vase_detail.html'

# create new vase
class VaseCreate(CreateView):
  model = Vase
  fields = '__all__'
  template_name = 'flower/vase_form.html'

# update the vase
class VaseUpdate(UpdateView):
  model = Vase
  fields = ['name', 'color']
  template_name = 'flower/vase_form.html'

# delete a vase
class VaseDelete(DeleteView):
  model = Vase
  template_name = 'flower/vase_delete.html'
  success_url = '/vase/'

