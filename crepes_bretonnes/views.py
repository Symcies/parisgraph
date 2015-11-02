from spots.models import Spot
from django.shortcuts import render
from spots.serializers import SpotSerializer
from django.core import serializers

def accueil2(request):    
    imported_spots = Spot.objects.all()
    
    return render(request, 'nogit.html', {'lieux':imported_spots})
    
def accueil(request):
    imported_spots = Spot.objects.all()
    
    lieux = serializers.serialize("json", Spot.objects.all())
    return render(request, 'nogit.html', {'lieux':lieux})