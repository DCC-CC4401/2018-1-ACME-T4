from django.db import models

from articlesApp.models import Article
from mainApp.models import Action
from spacesApp.models import Space


class Reservation(Action):
    STATES = (
        ('A', 'Aceptado'),
        ('R', 'Rechazado'),
        ('P', 'Pendiente')
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    space = models.ForeignKey(Space, on_delete=models.CASCADE, null=True, blank=True)
    state = models.CharField('Estado', choices=STATES, max_length=1, default='P')
