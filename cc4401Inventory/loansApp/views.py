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
        if loan.state == 'A':
            loan.article.state = 'L'
            loan.article.save()
    return redirect('user_data', user_id=request.user.id)