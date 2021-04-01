from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Create
    path('flowers/add-flower', views.CreateFlower.as_view(), name='add_flower'),
    
    # Get all flowers
    path('flowers/', views.GetAll.as_view(), name='flowers'),

    # Get One
    path('flowers/<int:pk>/', views.FlowerDetail, name='detail'),

    # Update
    path('flowers/<int:pk>/edit/', views.EditFlower.as_view(), name='edit'),

    # Delete
    path('flowers/<int:pk>/delete/', views.DeleteFlower.as_view(), name='delete'),

    # post meal schedule
    path('flowers/<int:pk>/add_meal/', views.add_meal, name='add_meal'),
]