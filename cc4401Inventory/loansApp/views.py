from django.shortcuts import render, redirect
from .models import Loan
from django.contrib import messages

def loan_data(request, loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        context = {
            'loan': loan,
        }

        return render(request, 'loan_data.html', context)
    except Exception as e:
        print(e)
        return redirect('/')

def modify_loans(request):
    if request.method == "POST":
        loan_id = request.POST.get('loan')
        loan = Loan.objects.get(id=loan_id)
        try:
            user = request.user
            if loan.user == user:
                if loan.state == 'A':
                    loan.article.state = 'L'
                    loan.article.save()
            else:
                messages.warning(request, 'Ud no puede realizar esta accion')
        except:
            messages.warning(request, 'Ha ocurrido un error y no se ha realizado la accion')        
        return redirect('user_data', user_id=request.user.id)