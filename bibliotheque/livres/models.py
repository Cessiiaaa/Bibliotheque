from django.db import models

from django.contrib.auth.models import User

# Create your models here.

GENRES_CHOIX = [
    ('aventure', 'Aventure'),
    ('biographie', 'Biographie'),
    ('fantastique', 'Fantastique'),
    ('histoire', 'Histoire'),
    ('horreur', 'Horreur'),
    ('policier', 'Policier'),
    ('roman', 'Roman'),
    ('science_fiction', 'Science-Fiction'),
    ('thriller', 'Thriller'),
]

class Livre(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=50)
    genre = models.TextField(max_length=50, choices=GENRES_CHOIX)
    description = models.CharField(max_length=200)
    date_de_publication = models.DateField()
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titre} - {self.auteur}"
