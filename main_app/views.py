from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Flower, Vase
from .forms import MealForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



# Define the about view
def home(request):
    return render (request, 'about.html')

# create
class CreateFlower(CreateView):
    model = Flower
    template_name = 'flower/add_form.html'
    fields = ['name', 'species', 'description']
  # This inherited method is called when a
  # valid cat form is being submitted
    def form_valid(self, form):
      # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
      # Let the CreateView do its job as usual
      return super().form_valid(form)


# Get All
def GetAll(request):
    model= Flower
    flowers = Flower.objects.filter(user=request.user)
    # You could also retrieve the logged in user's flowers like this
    return render(request, 'flower/flowers.html', { 'flowers': flowers })

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

# sign up new user
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)