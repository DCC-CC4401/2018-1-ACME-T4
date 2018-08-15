from django.shortcuts import render, redirect
from .models import Reservation
from django.contrib import messages

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

def cancel(request):
    if request.method == 'POST':
        reservation_id = request.POST.get('reservation')
        reservation = Reservation.objects.get(id=reservation_id)
        try:
            if reservation.state == 'P':
                reservation.delete()
        except:
            messages.warning(request, 'Ha ocurrido un error y la reserva no se ha cancelado')

        return redirect('user_data', user_id=request.user.id)
