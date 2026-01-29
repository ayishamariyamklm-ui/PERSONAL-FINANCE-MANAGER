"""
expense.py
Defines the Expense class for Personal Finance Manager
"""

class Expense:
    def __init__(self, amount, category, date, description):
        """
        Initialize an Expense object.

        Parameters:
        - amount (float): Amount spent
        - category (str): Category of expense (Food, Transport, etc.)
        - date (str): Date in YYYY-MM-DD format
        - description (str): Short description of expense
        """
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        """
        Return a human-readable string representation for CLI display.
        """
        return f"{self.date} | {self.category}: ₹{self.amount:.2f} - {self.description}"

