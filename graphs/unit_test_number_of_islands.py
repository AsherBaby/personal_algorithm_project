import unittest
from number_of_islands import numIslands

class TestNumIslands(unittest.TestCase):

    def test_of_small_datasets(self):
        grid = [
          [1, 1, 0, 0, 0],
          [0, 1, 0, 0, 1],
          [0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1]]
        self.assertEqual(
            numIslands(grid), 3)

if __name__ == '__main__':
    unittest.main()
