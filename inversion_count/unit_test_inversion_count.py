from inversion_count import inversion_count
import unittest

class TestInversionCount(unittest.TestCase):

    def test_of_size_one(self):
        array_a = [1]
        array_b = [1]
        self.assertEqual(inversion_count(array_a, array_b), 0)

    def test_of_size_two(self):
        array_a = [2, 1]
        array_b = [1, 2]
        self.assertEqual(inversion_count(array_a, array_b), 1)

    def test_of_size_three(self):
        array_a = [1, 3, 2]
        array_b = [2, 3, 1]
        self.assertEqual(inversion_count(array_a, array_b), 3)

if __name__ == '__main__':
    unittest.main()
