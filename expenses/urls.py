from django.urls import path
from .views import home, add_expense, export_expenses_to_excel, generate_qr_code

urlpatterns = [
    path('', home, name='home'),
    path('add-expense/', add_expense, name='add_expense'),
    path('export-expenses/', export_expenses_to_excel, name='export_expenses'),
    path('qr-code/', generate_qr_code, name='qr_code'),
]
