from django.http import HttpResponse
from django.shortcuts import render
from .models import *

def index(request):
    # Récupérer les objets de chaque modèle
    destination = Destination.objects.all()
    evenements_touristiques = EvenementTouristique.objects.all()
    transports = Transport.objects.all()
    restaurants = Restaurant.objects.all()
    hebergements = Hebergement.objects.all()

    # Ajouter les objets au contexte
    context = {
        'destinations': destination,
        'evenements_touristiques': evenements_touristiques,
        'transports': transports,
        'restaurants': restaurants,
        'hebergements': hebergements,
    }

    # Rendre le template avec le contexte
    return render(request, 'travele/index.html', context)
