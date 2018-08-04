from django.db import models

from mainApp.models import Action
from spacesApp.models import Space


class Reservation(Action):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
