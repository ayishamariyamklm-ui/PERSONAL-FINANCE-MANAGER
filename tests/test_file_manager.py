import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
import os
from src.expense import Expense
from src.file_manager import save_expenses, load_expenses, DATA_FILE


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.test_expenses = [
            Expense(100, "Food", "2024-01-01", "Breakfast"),
            Expense(200, "Transport", "2024-01-02", "Taxi")
        ]

    def test_save_and_load_expenses(self):
        save_expenses(self.test_expenses)
        loaded = load_expenses()

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].category, "Food")
        self.assertEqual(loaded[1].amount, 200.0)

    def tearDown(self):
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)


if __name__ == "__main__":
    unittest.main()
