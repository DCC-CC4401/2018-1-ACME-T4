from django.db import models

from reservationsApp.models import Reservation


class Loan(models.Model):
    STATES = (
        ('V', 'Vigente'),
        ('C', 'Caducado'),
        ('P', 'Perdido')
    )
    state = models.CharField('Estado', choices=STATES, max_length=1, default='V')
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, default=1)
