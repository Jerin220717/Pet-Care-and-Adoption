from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('pets/', views.pets, name='Pets'),
    path('adoption/', views.adoption, name='Adoption'),
    path('adoptionlist/', views.adoptionlist, name='Adoption List'),
    path('contact/', views.contact, name='Contact'),
    path('about/', views.about, name='About us'),
]