import unittest
from break_dollars import BreakDollars


class TestCombinationSum(unittest.TestCase):

    def test_of_break_ten_dollars(self):
        self.assertEqual(
            BreakDollars([1,2,5],10).solve(), 10)

    def test_of_break_one_hundard_dollars(self):
        self.assertEqual(
            BreakDollars([1,2,5,10,20,100],100).solve(), 4112)

if __name__ == '__main__':
    unittest.main()
