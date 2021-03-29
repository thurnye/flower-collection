from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/', views.flower_index, name='flower'),
    path('flowers/<int:flower_id>/', views.flower_detail, name='detail'),
]