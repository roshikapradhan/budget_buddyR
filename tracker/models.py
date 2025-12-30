from django.db import migrations, models
class BudgetGoal(models.Model):
    amount = models.FloatField()
    month = models.CharField(max_length=20) # e.g., "December"

    def __str__(self):
        return f"{self.month}: {self.amount}"
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food 🍔'),
        ('travel', 'Travel ✈️'),
        ('rent', 'Rent 🏠'),
        ('shopping', 'Shopping 🛍️'),
        ('bills', 'Bills 📄'),
        ('others', 'Others ✨'),
    ]
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
    