from django.db import models
from mainApp.models import User
from reservationsApp.models import ReservaArticulo
from reservationsApp.models import ReservaEspacio

class PrestamoArticulo(models.Model):
    reserva = models.ForeignKey(ReservaArticulo, on_delete=models.CASCADE)
    administrador = models.ForeignKey(User, on_delete=models.CASCADE)
    ESTADOS_PRES = ((1, 'Vigente'), (2, 'Caducado'), (3, 'Perdido'))
    estado_prestamo = models.IntegerField(choices=ESTADOS_PRES, default=1)

class PrestamoEspacio(models.Model):
    reserva = models.ForeignKey(ReservaEspacio, on_delete=models.CASCADE)
    administrador = models.ForeignKey(User, on_delete=models.CASCADE)
    ESTADOS_PRES = ((1, 'Vigente'), (2, 'Caducado'), (3, 'Perdido'))
    estado_prestamo = models.IntegerField(choices=ESTADOS_PRES, default=1)