import unittest
from flip_bits import flip_bits, flip_bits2

class Test(unittest.TestCase):

    def test_of_flip_bits(self):
        self.assertEqual(flip_bits('10010010'), 6)

    def test_of_flip_bits2(self):
        self.assertEqual(flip_bits('10010010'), 6)

if __name__ == '__main__':
    unittest.main()
