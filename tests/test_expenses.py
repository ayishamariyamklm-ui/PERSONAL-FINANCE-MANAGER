import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



import pytest
from src.expense import Expense


def test_expense_creation():
    expense = Expense(100, "Food", "2024-01-01", "Lunch")

    assert expense.amount == 100.0
    assert expense.category == "Food"
    assert expense.date == "2024-01-01"
    assert expense.description == "Lunch"
