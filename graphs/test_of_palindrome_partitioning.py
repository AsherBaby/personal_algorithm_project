import unittest
from palindrome_partitioning import partition

class TestPalindromePartitioning(unittest.TestCase):

    def test_of_null_string(self):
        self.assertEqual(
            partition(''),
            [[]])

    def test_of_small_string(self):
        self.assertEqual(
            partition('aab'),
            [['a', 'a', 'b'], ['aa', 'b']])

if __name__ == '__main__':
    unittest.main()
