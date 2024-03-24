from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    return render(request, 'petcare/home.html')
def pets(request):
    petList = models.Pet.objects.all()
    return render(request, 'petcare/pets.html', {'petList': petList})
def adoption(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        petType = request.POST['petType']
        description = request.POST['description']
        
        newEntry = models.AptionRequest(
            firstName = fname,
            lastName = lname,
            email = email,
            petType = petType,
            description = description
        )
        newEntry.save()
    return render(request, 'petcare/adoption.html')

def adoptionlist(request):
    adoptionlist = models.AptionRequest.objects.all()
    return render(request, 'petcare/adoptionlist.html', {'adoptions': adoptionlist})
def contact(request):
    return render(request, 'petcare/contact.html')
def about(request):
    return render(request, 'petcare/about.html')