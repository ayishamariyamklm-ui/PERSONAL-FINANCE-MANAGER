import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
from src.expense import Expense
from src.reports import category_summary, monthly_report


class TestReports(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense(100, "Food", "2024-01-01", "Breakfast"),
            Expense(200, "Food", "2024-01-02", "Lunch"),
            Expense(300, "Transport", "2024-01-03", "Taxi")
        ]

    def test_category_summary_runs(self):
        # Just checks it runs without error
        category_summary(self.expenses)

    def test_monthly_report_runs(self):
        monthly_report(self.expenses)


if __name__ == "__main__":
    unittest.main()
