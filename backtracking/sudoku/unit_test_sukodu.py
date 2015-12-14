import unittest
from sudoku import Sudoku

class TestSolveSudoku(unittest.TestCase):

    def test_of_empty_board(self):
        board = [
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None,],
        ]
        s = Sudoku(board)
        self.assertEqual(
            s.solve(),
            [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [4, 5, 6, 7, 8, 9, 1, 2, 3],
             [7, 8, 9, 1, 2, 3, 4, 5, 6],
             [2, 1, 4, 3, 6, 5, 8, 9, 7],
             [3, 6, 5, 8, 9, 7, 2, 1, 4],
             [8, 9, 7, 2, 1, 4, 3, 6, 5],
             [5, 3, 1, 6, 4, 2, 9, 7, 8],
             [6, 4, 2, 9, 7, 8, 5, 3, 1],
             [9, 7, 8, 5, 3, 1, 6, 4, 2]])


if __name__ == '__main__':
    unittest.main()
