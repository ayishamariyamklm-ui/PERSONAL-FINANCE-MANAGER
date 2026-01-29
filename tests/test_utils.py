import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
from src.utils import validate_amount, validate_category, validate_date


class TestUtils(unittest.TestCase):

    def test_validate_amount(self):
        self.assertTrue(validate_amount("100"))
        self.assertTrue(validate_amount(50))
        self.assertFalse(validate_amount("-10"))
        self.assertFalse(validate_amount("abc"))

    def test_validate_category(self):
        self.assertTrue(validate_category("Food"))
        self.assertTrue(validate_category("transport"))
        self.assertFalse(validate_category("InvalidCategory"))

    def test_validate_date(self):
        self.assertTrue(validate_date("2024-01-15"))
        self.assertFalse(validate_date("15-01-2024"))
        self.assertFalse(validate_date("2024/01/15"))


if __name__ == "__main__":
    unittest.main()
