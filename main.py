"""
main.py
Main entry point for the Personal Finance Manager application
"""

from src.expense import Expense
from src.file_manager import save_expenses, load_expenses, backup_data
from src.reports import (
    category_summary,
    monthly_report,
    search_expenses,
    category_bar_chart,
    monthly_trend_chart
)
from src.utils import validate_amount, validate_category, validate_date, pause
from src.menu import (
    display_main_menu,
    display_add_expense_menu,
    display_all_expenses_header,
    display_charts_menu,
    invalid_choice_message,
    exit_message
)


def add_new_expense(expenses):
    """
    Handles adding a new expense with input validation
    """
    display_add_expense_menu()

    try:
        # Amount input
        amount = input("Enter amount: ").strip()
        if not validate_amount(amount):
            print("❌ Amount must be a positive number.")
            pause()
            return
        amount = float(amount)

        # Category input
        category = input(
            "Enter category (Food/Transport/Entertainment/Shopping/Other): "
        ).strip().title()
        if not validate_category(category):
            print("❌ Invalid category.")
            pause()
            return

        # Date input
        date = input("Enter date (YYYY-MM-DD): ").strip()
        if not validate_date(date):
            print("❌ Invalid date format.")
            pause()
            return

        # Description input
        description = input("Enter description: ").strip()

        # Create Expense object
        expense = Expense(amount, category, date, description)
        expenses.append(expense)

        # Save to CSV
        save_expenses(expenses)
        print("\n✅ Expense added successfully!")

    except Exception as e:
        print(f"❌ Error adding expense: {e}")

    pause()


def view_all_expenses(expenses):
    """
    Display all expenses in a formatted list
    """
    display_all_expenses_header()

    if not expenses:
        print("No expenses found.")
    else:
        for exp in expenses:
            print(exp)

    pause()


def main():
    """
    Main loop of the Personal Finance Manager
    """
    expenses = load_expenses()

    while True:
        display_main_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            add_new_expense(expenses)

        elif choice == "2":
            view_all_expenses(expenses)

        elif choice == "3":
            category_summary(expenses)
            pause()

        elif choice == "4":
            monthly_report(expenses)
            pause()

        elif choice == "5":
            search_expenses(expenses)
            pause()

        elif choice == "6":
            backup_data()
            print("✅ Backup completed successfully!")
            pause()

        elif choice == "7":
            display_charts_menu()
            chart_choice = input("Choose option (1-2): ").strip()
            if chart_choice == "1":
                category_bar_chart(expenses)
            elif chart_choice == "2":
                monthly_trend_chart(expenses)
            else:
                print("❌ Invalid chart option.")
            pause()

        elif choice == "8":
            save_expenses(expenses)
            exit_message()
            break

        else:
            invalid_choice_message()
            pause()


if __name__ == "__main__":
    main()
