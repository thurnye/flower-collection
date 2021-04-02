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

    # Create Vase
    path('vase/create/', views.VaseCreate.as_view(), name='vase_create'),

    # associate a Vase with a flower (M:M)
    path('cats/<int:flower_id>/assoc_vase/<int:vase_id>/', views.assoc_vase, name='assoc_vase'),
    
    # unassociate a Vase and flower
    path('cats/<int:flower_id>/unassoc_vase/<int:vase_id>/', views.unassoc_vase, name='unassoc_vase'),

    path('vase/', views.VaseList.as_view(), name='vase_index'),

    path('vase/<int:pk>/', views.VaseDetail.as_view(), name='vase_detail'),

    path('vase/<int:pk>/update/', views.VaseUpdate.as_view(), name='vase_update'),

    path('vase/<int:pk>/delete/', views.VaseDelete.as_view(), name='vase_delete'),
]