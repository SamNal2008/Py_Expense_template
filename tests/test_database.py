import csv
import unittest
from expense import new_expense

class TestDatabase(unittest.TestCase):

    def test_store_new_expense(self, testcase={'amount': 23, 'label': 'toto', 'spender': 'pchojka'}, filename='test_expense_report.csv'):
      ref_header = tuple(testcase)
      ref_values = tuple(testcase.values())
      new_expense(*ref_values)
      ref_header = list(ref_header)
      ref_values = list(ref_values)
      ref_values[0] = str(ref_values[0])
      with open(filename, 'r') as f:
        reader = csv.reader(f)
        self.assertEqual(next(reader), ref_header)
        self.assertEqual(next(reader), list(ref_values))

