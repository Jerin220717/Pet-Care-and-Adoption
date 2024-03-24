from django.db import models

# Create your models here.
class Pet(models.Model):
    PetTypes = {
        'Cat': 'Cat',
        'Dog': 'Dog',
        'Bird': 'Bird',
        'Rabbit': 'Rabbit',
        'Hamster': 'Hamster',
        'Duck': 'Duck',
        'Other': 'Other'
    }
    petName = models.CharField(max_length=100, choices = PetTypes)
    petBreed = models.CharField(max_length=100)
    petInfo = models.TextField()
    petTips = models.TextField()
    imageUrl = models.CharField(max_length=255)
    

class AptionRequest(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    petType = models.CharField(max_length=100)
    description = models.TextField(default='')