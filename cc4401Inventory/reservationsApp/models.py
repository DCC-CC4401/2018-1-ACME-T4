from django.db import models
from mainApp.models import Item
from mainApp.models import User

class ReservaArticulo(models.Model):
    articulo = models.ForeignKey(Item, on_delete=models.CASCADE)
    perfil = models.ForeignKey(User, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    ESTADOS_RES = ((1, 'Pendiente'), (2, 'Entregado'), (3, 'Rechazado'))
    estado_reserva = models.IntegerField(choices=ESTADOS_RES, default=1)

    def __lt__(self, other):
        return self.final < other.final

    def get_cname(self):
        class_name = self.__class__.__name__
        return class_name

class ReservaEspacio(models.Model):
    espacio = models.ForeignKey(Item, on_delete=models.CASCADE)
    perfil = models.ForeignKey(User, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    ESTADOS_RES = ((1, 'Pendiente'), (2, 'Entregado'), (3, 'Rechazado'))
    estado_reserva = models.IntegerField(choices=ESTADOS_RES, default=1)

    def get_cname(self):
        class_name = self.__class__.__name__
        return class_name

