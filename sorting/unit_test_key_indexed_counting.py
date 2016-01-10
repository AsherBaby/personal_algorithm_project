import unittest
from key_indexed_counting import key_indexed_counting

class TestOfKeyIndexedCounting(unittest.TestCase):

    def test_of_small_array(self):
        a = ['z', 'b', 'r', 'p', 'e', 'a', 'k']
        key_indexed_counting(a)
        self.assertEqual(a, ['a', 'b', 'e', 'k', 'p', 'r', 'z'])

if __name__ == '__main__':
    unittest.main()
