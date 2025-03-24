from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
import pandas as pd
from django.http import HttpResponse
import qrcode
from io import BytesIO

def home(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'expenses/home.html', {'expenses': expenses})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def export_expenses_to_excel(request):
    expenses = Expense.objects.all().values()
    df = pd.DataFrame(expenses)
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=expenses.xlsx'
    
    if not df.empty:
        df.rename(columns={'date': 'Date', 'amount': 'Amount', 'category': 'Category', 
                           'payment_method': 'Payment Method', 'notes': 'Notes'}, inplace=True)
        df.to_excel(response, index=False, engine='openpyxl')
    
    return response

def generate_qr_code(request):
    qr = qrcode.make('http://127.0.0.1:8000/add-expense/')  # Update for deployment
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return HttpResponse(buffer.getvalue(), content_type="image/png")
