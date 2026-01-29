"""
utils.py
Utility functions for Personal Finance Manager
- Input validation
- User interaction helpers
"""

from datetime import datetime

# Allowed categories
ALLOWED_CATEGORIES = ["Food", "Transport", "Entertainment", "Shopping", "Other"]


def validate_amount(amount):
    """
    Validates that the amount is a positive number
    """
    try:
        amount = float(amount)
        return amount > 0
    except (ValueError, TypeError):
        return False


def validate_category(category):
    """
    Validates that the category is one of the allowed categories
    """
    if category.strip().title() in ALLOWED_CATEGORIES:
        return True
    return False


def validate_date(date_str):
    """
    Validates that the date is in YYYY-MM-DD format
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def pause():
    """
    Pause the program until the user presses Enter
    """
    input("\nPress Enter to continue...")

