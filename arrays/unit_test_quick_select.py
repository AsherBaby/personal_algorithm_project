import random
import unittest
from quick_select import quick_select

class TestOfQuickSelect(unittest.TestCase):

    def test_of_size_1(self):
        A = random.sample(range(10000), 2000)
        sorted_A = sorted(A)
        for i in range(len(A)):
            self.assertEqual(
                quick_select(A, i),
                sorted_A[i])

if __name__ == '__main__':
    unittest.main()
