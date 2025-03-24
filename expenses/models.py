from django.db import models

class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.amount} ({self.category})"
