from django import forms
from .models import Expense

CATEGORY_CHOICES = [
    ('food', 'Food'),
    ('transport', 'Transport'),
    ('entertainment', 'Entertainment'),
    ('bills', 'Bills'),
    ('shopping', 'Shopping'),
    ('other', 'Other'),
]

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        )
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Expense
        fields = ['date', 'amount', 'category', 'payment_method', 'notes']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
