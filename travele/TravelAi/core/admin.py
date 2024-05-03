from django.contrib import admin
from .models import Destination, OffreSpeciale, EvenementTouristique, Transport, Restaurant, Hebergement

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'image')

@admin.register(OffreSpeciale)
class OffreSpecialeAdmin(admin.ModelAdmin):
    list_display = ('destination', 'offre_speciale')

@admin.register(EvenementTouristique)
class EvenementTouristiqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'date_debut', 'date_fin')
    list_filter = ('date_debut', 'date_fin')

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'type_transport', 'disponibilite', 'tarif')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'type_cuisine', 'tarif_moyen')

@admin.register(Hebergement)
class HebergementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'capacite', 'tarif')
