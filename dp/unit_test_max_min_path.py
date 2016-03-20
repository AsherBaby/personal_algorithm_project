import unittest
from max_min_path import max_min_path

class TestMaxMinPath(unittest.TestCase):

    def test1(self):
        A = [[6, 5, 2],
             [7, 5, 4],
             [9, 2, 6]]
        self.assertEqual(max_min_path(A), 5)

    def test2(self):
        A = [[5, 7, 2],
             [7, 5, 8],
             [9, 1, 5]]
        self.assertEqual(max_min_path(A), 7)

if __name__ == '__main__':
    unittest.main()
