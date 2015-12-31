import unittest
from word_search import exist

class TestSomePackage(unittest.TestCase):

    def test_of_small_dataset(self):
        board = ["ABCE",
                 "SFCS",
                 "ADEE"]
        word = 'ESCEE'
        self.assertEqual(
            exist(board, word), True)

if __name__ == '__main__':
    unittest.main()
