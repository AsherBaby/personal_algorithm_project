import unittest
from num_of_palindromes import num_of_palindromes

class TestNumOfPalindromes(unittest.TestCase):

    def test_of_size_3(self):
        self.assertEqual(
            num_of_palindromes('aba'), 4)

    def test_of_size_4(self):
        self.assertEqual(
            num_of_palindromes('abba'), 6)

if __name__ == '__main__':
    unittest.main(verbosity=2)
