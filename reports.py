"""
reports.py
Handles all report generation, analysis, and visualization
"""

from collections import defaultdict
import matplotlib.pyplot as plt


def category_summary(expenses):
    """
    Display category-wise total expenses (text output)
    """
    if not expenses:
        print("\nNo expenses available to generate summary.")
        return

    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount

    print("\n--- CATEGORY-WISE SUMMARY ---")
    for category, total in summary.items():
        print(f"{category}: ₹{total:.2f}")


def category_bar_chart(expenses):
    """
    Display category-wise expense bar chart
    """
    if not expenses:
        print("\nNo expenses available for chart.")
        return

    summary = defaultdict(float)
    for exp in expenses:
        summary[exp.category] += exp.amount

    categories = list(summary.keys())
    amounts = list(summary.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts)
    plt.title("Category-wise Expenses")
    plt.xlabel("Category")
    plt.ylabel("Amount (₹)")
    plt.tight_layout()
    plt.show()


def monthly_report(expenses):
    """
    Generate text-based monthly expense report
    """
    if not expenses:
        print("\nNo expenses available to generate monthly report.")
        return

    monthly_data = defaultdict(list)

    for exp in expenses:
        month = exp.date[:7]  # YYYY-MM
        monthly_data[month].append(exp.amount)

    print("\n--- MONTHLY REPORT ---")
    for month, amounts in monthly_data.items():
        total = sum(amounts)
        average = total / len(amounts)
        print(
            f"{month} | Total: ₹{total:.2f} | "
            f"Average: ₹{average:.2f} | Entries: {len(amounts)}"
        )


def monthly_trend_chart(expenses):
    """
    Display monthly expense trend line chart
    """
    if not expenses:
        print("\nNo expenses available for trend chart.")
        return

    summary = defaultdict(float)

    for exp in expenses:
        month = exp.date[:7]  # YYYY-MM
        summary[month] += exp.amount

    months = sorted(summary.keys())
    totals = [summary[m] for m in months]

    plt.figure(figsize=(8, 5))
    plt.plot(months, totals, marker="o")
    plt.title("Monthly Expense Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def search_expenses(expenses, keyword):
    """
    Search expenses by description or category
    """
    keyword = keyword.lower()
    results = []

    for exp in expenses:
        if (
            keyword in exp.description.lower()
            or keyword in exp.category.lower()
        ):
            results.append(exp)

    return results


