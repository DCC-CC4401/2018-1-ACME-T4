from django.db import models

from mainApp.models import Item


class Space(Item):
    STATES = (
        ('D', 'Disponible'),
        ('P', 'En préstamo'),
        ('R', 'En reparación')
    )
    state = models.CharField(max_length=1, choices=STATES)
    is_quincho = models.BooleanField(default=False)
