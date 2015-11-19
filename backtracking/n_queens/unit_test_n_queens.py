import unittest
from n_queens import solveNQueens

class TestSolveNQueens(unittest.TestCase):

    def test_of_2_queens(self):
        self.assertEqual(
            solveNQueens(2),
            [])

    def test_of_3_queens(self):
        self.assertEqual(
            solveNQueens(3),
            [])

    def test_of_4_queens(self):
        self.assertEqual(
            solveNQueens(4),
            [['..Q.', 'Q...', '...Q', '.Q..'],
            ['.Q..', '...Q', 'Q...', '..Q.']])

if __name__ == '__main__':
    unittest.main()
