from django.shortcuts import render, redirect
from .models import Reservation
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def reservation_data(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id)
        context = {
            'reservation': reservation,
        }

        return render(request, 'reservation_data.html', context)
    except Exception as e:
        print(e)
        return redirect('/')

def delete(request):
    if request.method == 'POST':
        reservation_ids = request.POST.getlist('reservation')
        try:
            for reservation_id in reservation_ids:
                reservation = Reservation.objects.get(id=reservation_id)
                if reservation.state == 'P':
                    reservation.delete()
        except:
            messages.warning(request, 'Ha ocurrido un error y la reserva no se ha eliminado')

        return redirect('user_data', user_id=request.user.id)

@login_required
def cancel(request):
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation')
        reservation = Reservation.objects.get(id=reservation_id)
        try:
            user = request.user
            if reservation.user == user:
                if reservation.state == 'P':
                    reservation.delete()
            else:
                messages.warning(request, 'Ud no puede cancelar esta reserva')
        except:
            messages.warning(request, 'Ha ocurrido un error y la reserva no se ha cancelado')

        return redirect('user_data', user_id=request.user.id)
