from django.db import models

from articlesApp.models import Article
from mainApp.models import User
from spacesApp.models import Space


class Reservation(models.Model):
    STATES = (
        ('A', 'Aceptado'),
        ('R', 'Rechazado'),
        ('P', 'Pendiente')
    )
    TYPES = (
        ('A', 'Articulo'),
        ('S', 'Espacio')
    )
    starting_date_time = models.DateTimeField()
    ending_date_time = models.DateTimeField()
    state = models.CharField('Estado', choices=STATES, max_length=1, default='P')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    type = models.CharField('Tipo', choices=TYPES, max_length=1, default='A')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE, blank=True, null=True)
