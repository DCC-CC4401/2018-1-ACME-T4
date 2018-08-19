from django.shortcuts import render
from django.utils.timezone import localtime
import datetime
from articlesApp.models import Article
from spacesApp.models import Space
from django.contrib import messages
from reservationsApp.models import Reservation
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



@login_required
def landing_articles(request):
    context = {}
    return render(request, 'articulos.html', context)


@login_required
def landing_spaces(request, date=None):
    if date:
        current_date = date
        current_week = datetime.datetime.strptime(current_date, "%Y-%m-%d").date().isocalendar()[1]
    else:
        try:
            current_week = datetime.datetime.strptime(request.POST["date"], "%Y-%m-%d").date().isocalendar()[1]
            current_date = request.POST["date"]
        except:
            current_week = datetime.date.today().isocalendar()[1]
            current_date = datetime.date.today().strftime("%Y-%m-%d")

    reservations = Reservation.objects.filter(starting_date_time__week=current_week, state__in=['P', 'A'])
    colores = {'A': 'rgba(0,153,0,0.7)',
               'P': 'rgba(51,51,204,0.7)'}



    try:
        filter_list = []
        for s in Space.objects.all():
            filter_list.append(request.POST[s.name])
        res_list =[]
        for i in range(5):
            res_list.append(list())
        for r in reservations:
            if r.space.name in filter_list:
                reserv = []
                reserv.append(r.space.name)
                reserv.append(localtime(r.starting_date_time).strftime("%H:%M"))
                reserv.append(localtime(r.ending_date_time).strftime("%H:%M"))
                reserv.append(colores[r.state])
                res_list[r.starting_date_time.isocalendar()[2] - 1].append(reserv)
    except:
        filter_list=[]
        for s in Space.objects.all():
            filter_list.append(s.name)
        res_list = []
        for i in range(5):
            res_list.append(list())
        for r in reservations:
            reserv = []
            reserv.append(r.space.name)
            reserv.append(localtime(r.starting_date_time).strftime("%H:%M"))
            reserv.append(localtime(r.ending_date_time).strftime("%H:%M"))
            reserv.append(colores[r.state])
            res_list[r.starting_date_time.isocalendar()[2] - 1].append(reserv)
    #########################



    move_controls = list()
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=-4)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=-1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=1)).strftime("%Y-%m-%d"))
    move_controls.append(
        (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(weeks=4)).strftime("%Y-%m-%d"))

    delta = (datetime.datetime.strptime(current_date, "%Y-%m-%d").isocalendar()[2]) - 1
    monday = (
    (datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta)).strftime("%d/%m/%Y"))
    lunes = (
    (datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta)).strftime("%d/%m/%Y"))
    martes = (
    (datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta - 1)).strftime("%d/%m/%Y"))
    miercoles = (
    (datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta - 2)).strftime("%d/%m/%Y"))
    jueves = (
    (datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta - 3)).strftime("%d/%m/%Y"))
    viernes = (
    (datetime.datetime.strptime(current_date, "%Y-%m-%d") - datetime.timedelta(days=delta - 4)).strftime("%d/%m/%Y"))

    spaces = Space.objects.all()
    context = {'reservations': res_list,
               'current_date': current_date,
               'controls': move_controls,
               'actual_monday': monday,
               'monday': lunes,
               'tuesday': martes,
               'wednesday': miercoles,
               'thursday': jueves,
               'friday': viernes,
               'espacios': spaces,
               'filtros':filter_list}

    return render(request, 'espacios.html', context)



@login_required
def landing_search(request, products):
    if not products:
        return landing_articles(request)
    else:
        context = {'productos' : products,
                   'colores' : {'D': '#009900',
                                'R': '#ffcc00',
                                'P': '#3333cc',
                                'L': '#cc0000'}
                   }
        return render(request, 'articulos.html', context)


@login_required
def search(request):
    if request.method == "GET":
        query = request.GET['query']
        #a_type = "comportamiento_no_definido"
        a_state = "A" if (request.GET['estado'] == "A") else request.GET['estado']

        if not (a_state == "A"):
            articles = Article.objects.filter(state=a_state,name__icontains=query.lower())
        else:
            articles = Article.objects.filter(name__icontains=query.lower())

        products = None if (request.GET['query'] == "") else articles
        return landing_search(request, products)

@login_required
def space_request(request):
    if request.method == 'POST':
        space=Space.objects.get(name= request.POST['espacio'])              #  request.POST['espacio']  ==nombre del espacio
        hora_inicial= request.POST['hora_inicial']# hora en string
        hora_final=request.POST['hora_final']# hora en string
        fecha= request.POST['fecha'] #fecha en string
        string_inicio=fecha + " " + hora_inicial
        start_date_time= datetime.datetime.strptime(string_inicio, '%d/%m/%Y %H:%M')
        string_fin=fecha + " " + hora_final
        end_date_time= datetime.datetime.strptime(string_fin, '%d/%m/%Y %H:%M')

        if start_date_time < datetime.datetime.now() + datetime.timedelta(hours=1):
                    messages.warning(request, 'Los pedidos deben ser hechos al menos con una hora de anticipación.')
        elif Reservation.objects.filter(
                space=Space.objects.get(name= request.POST['espacio']),starting_date_time__lt=end_date_time,
                                        ending_date_time__gt=end_date_time) .count()>0:
            messages.warning(request, 'Este espacio ya está pedido en el horario seleccionado.')
        elif Reservation.objects.filter(
                space=Space.objects.get(name= request.POST['espacio']),starting_date_time__lt=start_date_time,
                                        ending_date_time__gt=start_date_time) .count()>0:
            messages.warning(request, 'Este espacio ya está pedido en el horario seleccionado.')
        elif Reservation.objects.filter(
                space=Space.objects.get(name= request.POST['espacio']),starting_date_time__gt=start_date_time,
                                        ending_date_time__lt=end_date_time) .count()>0:
            messages.warning(request, 'Este espacio ya está pedido en el horario seleccionado.')
        elif Reservation.objects.filter(
                space=Space.objects.get(name= request.POST['espacio']),starting_date_time__lt=start_date_time,
                                        ending_date_time__gt=end_date_time) .count()>0:
            messages.warning(request, 'Este espacio ya está pedido en el horario seleccionado.')
        else:
            reservation = Reservation(space=space, starting_date_time=start_date_time,
                                      ending_date_time=end_date_time,
                                      user=request.user)
            reservation.save()
            messages.success(request, 'Pedido realizado con éxito')


    return redirect('landing_spaces')

@login_required
def check_user(request):
    user=request.user
    if user.is_staff:
        return redirect("landing-panel")
    else:
        return redirect ('landing')
