import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
import matplotlib
# Use a non-GUI backend for testing
matplotlib.use("Agg")

from src.expense import Expense
from src.reports import category_bar_chart, monthly_trend_chart


class TestMatplotlibCharts(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense(100, "Food", "2024-01-01", "Breakfast"),
            Expense(200, "Food", "2024-01-02", "Lunch"),
            Expense(300, "Transport", "2024-02-01", "Taxi"),
        ]

    def test_category_bar_chart_runs(self):
        """
        Test that category bar chart runs without errors
        """
        try:
            category_bar_chart(self.expenses)
        except Exception as e:
            self.fail(f"category_bar_chart raised an exception: {e}")

    def test_monthly_trend_chart_runs(self):
        """
        Test that monthly trend chart runs without errors
        """
        try:
            monthly_trend_chart(self.expenses)
        except Exception as e:
            self.fail(f"monthly_trend_chart raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
