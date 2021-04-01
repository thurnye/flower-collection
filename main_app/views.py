from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower
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
  # instantiate MealForm to be rendered in the template
  meal_form = MealForm()
  return render(request, 'flower/detail.html', {
    'flower': flower, 'meal_form': meal_form
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
    # else:
    #     error_message = 'Invalid sign up - try again'
    #     # A bad POST or a GET request, so render signup.html with an empty form
    #     form = MealForm()
    #     context = {'form': form, 'error_message': error_message}
    #     return redirect('detail', pk=pk)



