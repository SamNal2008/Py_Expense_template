import unittest

from .test_expense import TestExpense


def suite():
    suite = unittest.TestSuite()
    TestExpense.test_add_expense()
    return suite

def test_main():
  runner = unittest.TextTestRunner()
  runner.run(suite())

if __name__ == '__main__':
    test_main()