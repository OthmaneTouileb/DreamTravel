from django.db import models

class Destination(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')

    def __str__(self):
        return self.nom

class OffreSpeciale(models.Model):
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE)
    offre_speciale = models.BooleanField(default=False)

class EvenementTouristique(Destination):
    date_debut = models.DateField()
    date_fin = models.DateField()
    offre_speciale = models.OneToOneField(OffreSpeciale, on_delete=models.CASCADE, null=True, blank=True)

class Transport(Destination):
    TYPE_CHOICES = [
        ('Car', 'Car'),
        ('Train', 'Train'),
        ('Avion', 'Avion'),
        ('Bateau', 'Bateau'),
    ]
    type_transport = models.CharField(max_length=10, choices=TYPE_CHOICES)
    disponibilite = models.BooleanField(default=True)
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
    offre_speciale = models.OneToOneField(OffreSpeciale, on_delete=models.CASCADE, null=True, blank=True)

class Restaurant(Destination):
    type_cuisine = models.CharField(max_length=100)
    tarif_moyen = models.DecimalField(max_digits=10, decimal_places=2)
    offre_speciale = models.OneToOneField(OffreSpeciale, on_delete=models.CASCADE, null=True, blank=True)

class Hebergement(Destination):
    capacite = models.IntegerField()
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
    offre_speciale = models.OneToOneField(OffreSpeciale, on_delete=models.CASCADE, null=True, blank=True)
