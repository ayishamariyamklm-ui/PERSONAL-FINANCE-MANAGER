"""
file_manager.py
Handles all file operations for Personal Finance Manager:
- Load expenses from CSV
- Save expenses to CSV
- Backup data
"""

import csv
import os
from .expense import Expense

# Default data file path
DATA_FILE = "data/expenses.csv"
BACKUP_FILE = "data/expenses_backup.csv"


def load_expenses():
    """
    Load expenses from the CSV file and return a list of Expense objects.
    Returns an empty list if file does not exist.
    """
    expenses = []

    # Check if file exists
    if not os.path.exists(DATA_FILE):
        return expenses

    try:
        with open(DATA_FILE, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Skip incomplete rows
                if row["Amount"] and row["Category"] and row["Date"] and row["Description"]:
                    expense = Expense(
                        amount=row["Amount"],
                        category=row["Category"],
                        date=row["Date"],
                        description=row["Description"]
                    )
                    expenses.append(expense)
    except Exception as e:
        print(f"Error loading expenses: {e}")

    return expenses


def save_expenses(expenses):
    """
    Save a list of Expense objects to the CSV file.
    Overwrites the existing file.
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["Date", "Category", "Amount", "Description"])
            # Write rows
            for exp in expenses:
                writer.writerow([exp.date, exp.category, exp.amount, exp.description])
    except Exception as e:
        print(f"Error saving expenses: {e}")


def backup_data():
    """
    Create a backup of the current expenses CSV file.
    """
    if not os.path.exists(DATA_FILE):
        print("No data to backup.")
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as original, \
             open(BACKUP_FILE, "w", encoding="utf-8") as backup:
            backup.write(original.read())
        print(f"✅ Backup created at {BACKUP_FILE}")
    except Exception as e:
        print(f"Error creating backup: {e}")
