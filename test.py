import unittest
from main import isOdd, isEven

class TestEvenOdd(unittest.TestCase):
    def test_odd(self):
        self.assertTrue(isOdd(1))
    def test_even(self):
        self.assertTrue(isEven(2))
if __name__ == '__main__':
    unittest.main()