import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from loansApp.models import Loan
from mainApp.models import User
from reservationsApp.models import Reservation


def login_view(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'usersApp/login.html', context=context)
    if request.method == 'POST':
        pass


# se llama cuando se envia el formulario de login
def login_submit(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'error_message': ''}

    if user is not None:
        # Se rechazan reservas al quincho, estas caducan 24 horas antes de su fecha de inicio
        query = Reservation.objects.filter(user=user, type='S', state='P', space__is_quincho=True)
        for reservation in query:
            if reservation.starting_date_time >= datetime.datetime.now() - datetime.timedelta(hours=24):
                reservation.state = 'R'
                reservation.save()

        if user.is_superuser:
            login(request, user)
            return redirect('/admin/')
        else:
            login(request, user)
            return redirect('/articles/')
    else:
        messages.warning(request, 'La contraseña ingresada no es correcta o el usuario no existe')
        return redirect('/user/login')


# se llama cuando se quiere acceder a la pagina de creacion de cuentas
def signup(request):
    if request.method == 'GET':
        return render(request, 'usersApp/create_account.html')
    if request.method == 'POST':
        pass


# se llama cuando se manda el formulario de creacion de cuentas
def signup_submit(request):
    context = {'error_message': '', }

    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        rut = request.POST['RUT']

        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Ya existe una cuenta con ese correo.')
            return redirect('/user/signup/')
        elif User.objects.filter(rut=rut).exists():
            messages.warning(request, 'Ya existe una cuenta con ese rut')
            return redirect('/user/signup/')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password,
                                            rut=rut)
            login(request, user)
            messages.success(request, 'Bienvenid@, ' + user.first_name + ' ya puedes comenzar a hacer reservas :)')
            if user.is_superuser:
                return redirect('/admin/')
            return redirect('/articles/')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/user/login/')


@login_required
def user_data(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        reservations = Reservation.objects.filter(user=user_id).order_by('-starting_date_time')[:10]
        loans = Loan.objects.filter(user=user_id).order_by('-starting_date_time')[:10]

        context = {
            'user': user,
            'reservations': reservations,
            'loans': loans
        }
        return render(request, 'usersApp/user_profile.html', context)
    except Exception:
        return redirect('/')
