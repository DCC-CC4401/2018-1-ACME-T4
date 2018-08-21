from django.db import models

from mainApp.models import Item


class Article(Item):
    STATES = (
        ('D', 'Disponible'),
        ('P', 'En préstamo'),
        ('R', 'En reparación'),
        ('L', 'Perdido')
    )
    state = models.CharField(max_length=1, choices=STATES, default='D')
