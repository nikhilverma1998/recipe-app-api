"""
sample tests
"""
from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test_add_numbers(self):
        """test of adding numbers"""
        res = calc.add(5,8)
        self.assertEqual(res,13)

    def test_subtract_numbers(self):
        """subtracting numbers"""
        res = calc.subtract(10,47)
        self.assertEqual(res,-37)